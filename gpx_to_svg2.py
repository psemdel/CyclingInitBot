#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:20:17 2020

@author: maxime
"""

#!/usr/bin/env python3

#   Copyright (c) 2012-2018 Tobias Leupold <tobias.leupold@gmx.de>
#
#   gpx2svg - Convert GPX formatted geodata to Scalable Vector Graphics (SVG)
#
#   This program is free software; you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the Free
#   Software Foundation in version 2 of the License.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#   or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#   for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

__version__ = '@VERSION@'

import argparse
import sys
import math
from xml.dom.minidom import parse as parseXml
from os.path import abspath
import gpx_parser as parser

def parseGpx(gpxFile):
    """Get the latitude and longitude data of all track segments in a GPX file"""

    if gpxFile == '/dev/stdin':
        gpxFile = sys.stdin

    # Get the XML information
    try:
        gpx = parseXml(gpxFile)
    except IOError as error:
        print('Error while reading file: {}. Terminating.'.format(error), file = sys.stderr)
        sys.exit(1)
    except:
        print('Error while parsing XML data:', file = sys.stderr)
        print(sys.exc_info(), file = sys.stderr)
        print('Terminating.', file = sys.stderr)
        sys.exit(1)

    # Iterate over all tracks, track segments and points
    gpsData = []
    for track in gpx.getElementsByTagName('trk'):
        for trackseg in track.getElementsByTagName('trkseg'):
            trackSegData = []
            for point in trackseg.getElementsByTagName('trkpt'):
                trackSegData.append(
                    (float(point.attributes['lon'].value), float(point.attributes['lat'].value))
                )
            # Leave out empty segments
            if(trackSegData != []):
                gpsData.append(trackSegData)

    return gpsData

def calcProjection(gpsData):
    """Calculate a plane projection for a GPS dataset"""

    projectedData = []
    for segment in gpsData:
        projectedSegment = []
        for coord in segment:
            # At the moment, we only have the Mercator projection
            projectedSegment.append(mercatorProjection(coord))
        projectedData.append(projectedSegment)

    return projectedData

def mercatorProjection(coord):
    """Calculate the Mercator projection of a coordinate pair"""

    # Assuming we're on earth, we have (according to GRS 80):
    r = 6378137.0

    # As long as meridian = 0 and can't be changed, we don't need:
    #    meridian = meridian * math.pi / 180.0
    #    x = r * ((coord[0] * math.pi / 180.0) - meridian)

    # Instead, we use this simplified version:
    x = r * coord[0] * math.pi / 180.0
    y = r * math.log(math.tan((math.pi / 4.0) + ((coord[1] * math.pi / 180.0) / 2.0)))
    return x, y

def moveProjectedData(gpsData):
    """Move a dataset to 0,0 and return it with the resulting width and height"""

    # Find the minimum and maximum x and y coordinates
    minX = maxX = gpsData[0][0][0]
    minY = maxY = gpsData[0][0][1]
    for segment in gpsData:
        for coord in segment:
            if coord[0] < minX:
                minX = coord[0]
            if coord[0] > maxX:
                maxX = coord[0]
            if coord[1] < minY:
                minY = coord[1]
            if coord[1] > maxY:
                maxY = coord[1]

    # Move the GPS data to 0,0
    movedGpsData = []
    for segment in gpsData:
        movedSegment = []
        for coord in segment:
            movedSegment.append((coord[0] - minX, coord[1] - minY))
        movedGpsData.append(movedSegment)

    # Return the moved data and it's width and height
    return movedGpsData, maxX - minX, maxY - minY

def searchCircularSegments(gpsData):
    """Splits a GPS dataset to tracks that are circular and other tracks"""

    circularSegments = []
    straightSegments = []

    for segment in gpsData:
        if segment[0] == segment[len(segment) - 1]:
            circularSegments.append(segment)
        else:
            straightSegments.append(segment)

    return circularSegments, straightSegments

def is_same_point(point1,point2):
    if point1[0]==point2[0] and  point1[1] ==point2[1]:
        return True
    else:
        return False


def splitSegments(gpsData):
    inlinepart=[]
    thislinecoord = []
    thiscircuit=[]
    allcircuit=[]
    reversepart=[]
    allreverse=[]
    pointscouple=[]
    
    incircuit=False
    inreverse=False
    lastpointstraight=False
    ff=0
        
    for coord in gpsData:
        print(len(coord))
        for ii in range(len(coord)):
            done=False
            for jj in range(ii+1, len(coord)) :
                if is_same_point(coord[ii],coord[jj]):
                   pointscouple.append([ii,jj,jj-ii,coord[ii]])
                   done=True
                   lastpointstraight=False
                   break
            if not done:
                if lastpointstraight==False and thislinecoord!=[]:
                    inlinepart.append(thislinecoord)
                    thislinecoord=[]
                thislinecoord.append(coord[ii])
                lastpointstraight=True
        inlinepart.append(thislinecoord)        

    lastdif=0
    lastpoint=0
    for pointcouple in pointscouple:
        if pointcouple[0]!=lastpoint:
            if  equaldif(pointcouple[2],lastdif) :
                incircuit=True
                inreverse=False
                thiscircuit.append(pointcouple[3])
            elif pointcouple[2]==lastdif-2:
                incircuit=False
                inreverse=True
                reversepart.append(pointcouple[3])
            else:
                incircuit=False
                inreverse=False
            lastpoint=pointcouple[0]
            lastdif=pointcouple[2]
            if incircuit==False and thiscircuit!=[]:
                allcircuit.append(thiscircuit)
                thiscircuit=[]
            elif inreverse==False and reversepart!=[]:
                allreverse.append(reversepart)
                reversepart=[]

    return inlinepart, allcircuit, allreverse

def equaldif(dif1, dif2):
    for kk in range(-5,5):
        if dif1==dif2+kk:
            return True
    if dif2!=0:
        if abs(dif1/dif2 - math.floor(dif1/dif2))<0.05:
            return True
        else:
            return False
    else:
        return False

def combineSegmentPairs(gpsData):
    """Combine segment pairs to one bigger segment"""

    combinedData = []
    # Walk through the GPS data and search for segment pairs
    # that end with the starting point of another track
    while len(gpsData) > 0:
        # Get one segment from the source GPS data
        firstTrackData = gpsData.pop()
        foundMatch = False

        # Try to find a matching segment
        for i in range(len(gpsData)):
            if firstTrackData[len(firstTrackData) - 1] == gpsData[i][0]:
                # There is a matching segment, so break here
                foundMatch = True
                break

        if foundMatch == True:
            # We found a pair of segments with one shared point, so pop the data of the second
            # segment from the source GPS data and create a new segment containing all data, but
            # without the overlapping point
            firstTrackData.pop()
            combinedData.append(firstTrackData + gpsData[i])
            gpsData.pop(i)
        else:
            # No segment with a shared point was found, so just append the data to the output
            combinedData.append(firstTrackData)

    return searchCircularSegments(combinedData)

def combineSegments(gpsData):
    """Combine all segments of a GPS dataset that can be combined"""

    # Search for circular segments. We can't combine them with any other segment.
    circularSegments, remainingSegments = searchCircularSegments(gpsData)

    # Search for segments that can be combined
    while True:
        # Look how many tracks we have now
        segmentsBefore = len(remainingSegments)
        # Search for segments that can be combined
        newCircularSegments, remainingSegments = combineSegmentPairs(remainingSegments)

        # Add newly found circular segments to processedSegments -- they can't be used anymore
        circularSegments = circularSegments + newCircularSegments

        if segmentsBefore == len(remainingSegments):
            # combineSegmentPairs() did not reduce the number of tracks anymore,
            # so we can't combine more tracks and can stop here
            break

    return circularSegments + remainingSegments

def chronologyJoinSegments(gpsData):
    """Join all segments to a big one in the order defined by the GPX file."""
    joinedSegment = []
    for segment in gpsData:
        joinedSegment += segment
    return [joinedSegment]

def scaleCoords(coord, height, scale):
    """Return a scaled pair of coordinates"""
    return coord[0] * scale, (coord[1] * -1 + height) * scale

def generateScaledSegment(segment, height, scale):
    """Create the coordinate part of an SVG path string from a GPS data segment"""
    for coord in segment:
        yield scaleCoords(coord, height, scale)

def writeSvgData(gpsData, width, height, maxPixels, dropSinglePoints, outfile):
    """Output the SVG data -- quick 'n' dirty, without messing around with dom stuff ;-)"""

    # Calculate the scale factor we need to fit the requested maximal output size
    if width <= maxPixels and height <= maxPixels:
        scale = 1
    elif width > height:
        scale = maxPixels / width
    else:
        scale = maxPixels / height

    # Open the requested output file or map to /dev/stdout
    if outfile != '/dev/stdout':
        try:
            fp = open(outfile, 'w')
        except IOError as error:
            print("Can't open output file: {}. Terminating.".format(error), file = sys.stderr)
            sys.exit(1)
    else:
        fp = sys.stdout

    # Header data
    fp.write( '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    fp.write(('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
              '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'))
    fp.write( '<!-- Created with gpx2svg {} -->\n'.format(__version__))
    fp.write(('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
              'width="{}px" height="{}px">\n').format(width * scale, height * scale))

    # Process all track segments and generate ids and path drawing commands for them

    # First, we split the data to circular and straight segments
   
    inlinepart, allcircuit, allreverse = splitSegments(gpsData)

    circularSegments, straightSegments = searchCircularSegments(gpsData)
    realCircularSegments = []
    singlePoints = []
    for segment in circularSegments:
        # We can leave out the last point, because it's equal to the first one
        segment.pop()
        if len(segment) == 1:
            # It's a single point
            if dropSinglePoints == False:
                # We want to keep single points, so add it to singlePoints
                singlePoints.append(segment)
        else:
            realCircularSegments.append(segment)

    circularSegments = realCircularSegments

    # Draw single points if requested
    if len(singlePoints) > 0:
        fp.write('<g>\n')
        for segment in singlePoints:
            x, y = scaleCoords(segment[0], height, scale)
            fp.write(
                '<circle cx="{}" cy="{}" r="0.5" style="stroke:none;fill:black"/>\n'.format(x, y)
            )
        fp.write('</g>\n')

    # Draw all circular segments
    if len(circularSegments) > 0:
        fp.write('<g>\n')
        for segment in circularSegments:
            fp.write('<path d="M')
            for x, y in generateScaledSegment(segment, height, scale):
                fp.write(' {} {}'.format(x, y))
            fp.write(' Z" style="fill:none;stroke:black"/>\n')
        fp.write('</g>\n')

       
    fp.write('<g inkscape:groupmode="layer" id="layer3" inkscape:label="Reverse">')
    print("start reverse") 
    if len(allreverse) > 0:
        for segment in allreverse:
            fp.write('<path d="M')
            for x, y in generateScaledSegment(segment, height, scale):
                fp.write(' {} {}'.format(x, y))
            fp.write('" style="fill:none;stroke:black;"/>\n')
    fp.write('</g>\n')    

    fp.write('<g inkscape:groupmode="layer" id="layer1" inkscape:label="Parcours">\n')
    print("start in line")
    # Draw all un-closed paths
    if len(inlinepart) > 0:
        for segment in inlinepart:
            fp.write('<path d="M')
            for x, y in generateScaledSegment(segment, height, scale):
                fp.write(' {} {}'.format(x, y))
            fp.write('" style="fill:none;stroke:#ff0000;stroke-width:3;inkscape:connector-curvature="0""/>\n') #stroke-opacity:1;stroke-width:3;stroke-miterlimit:4;
    fp.write('</g>\n')
    
    # Draw all un-closed paths
    fp.write('<g inkscape:groupmode="layer" id="layer2" inkscape:label="Circuit">\n')
    print("start circuits")
    if len(allcircuit) > 0:
      #  for circuit in allcircuit:
     #   fp.write('<g>\n')
        for segment in allcircuit:
            fp.write('<path d="M')
            for x, y in generateScaledSegment(segment, height, scale):
               fp.write(' {} {}'.format(x, y))
            fp.write(' Z" style="fill:none;stroke:#00007d;stroke-width:3;inkscape:connector-curvature="0""/>\n')
    fp.write('</g>\n') 

    # Close the XML
    fp.write('</svg>\n')

    # Close the file if necessary
    if fp != sys.stdout:
        fp.close()

def renamefile():
    os.rename(r'/home/maxime/Téléchargements/map',r'/home/maxime/Téléchargements/map.osm')
    
def loadgpx():
    with open('input/test.gpx', 'r') as gpx_file:
        gpx = parser.parse(gpx_file)
        print("{} tracks loaded".format(len(gpx)))    
    return gpx

def getminmax(gpx):
    minlat=1e6
    maxlat=0
    minlon=1e6
    maxlon=0
    verbose=False
    
    #get min max
    for track in gpx:
        for segment in track:
            for point in segment:
                if point.latitude>maxlat:
                    maxlat=point.latitude
                if point.latitude<minlat:
                    minlat=point.latitude
                if point.longitude>maxlon:
                    maxlon=point.longitude
                if point.longitude<minlon:
                    minlon=point.longitude
     
    minlat=round(minlat-0.01,4)    
    maxlat=round(maxlat+0.01,4) 
    minlon=round(minlon-0.01,4)     
    maxlon=round(maxlon+0.01,4) 
      
    if verbose:
        print("lat")
        print(minlat)
        print(maxlat)
        print("lon")
        print(minlon)
        print(maxlon)    
       
    return str(minlon) + "," + str(minlat) + "," +str(maxlon) + "," + str(maxlat) , minlat, maxlat, minlon, maxlon

def downloadmap(coord):
    url="download-osm-overpass bounds=" +coord
    #url="https://overpass-api.de/api/map?bbox=" + coord
    return url

def main():
    # Get the latitude and longitude data from the given GPX file or STDIN
    gpsData = parseGpx('input/test.gpx')
    
    gpx=loadgpx()
    coord, minlat, maxlat, minlon, maxlon=getminmax(gpx)
    
    print('first get map background')
    print('cd /disque1/Documents/Maperitive/')
    print('sh Maperitive.sh')
    print(downloadmap(coord))
    print("export-svg compatibility=inkscape")

    # Check if we actually _have_ data
    if gpsData == []:
        print('No data to convert. Terminating.', file = sys.stderr)
        sys.exit(1)

    # Try to combine all track segments that can be combined if not requested otherwise
    # Don't execute if all segments are already joined with "-j"
    gpsData = combineSegments(gpsData)

    # Calculate a plane projection for a GPS dataset
    # At the moment, we only have the Mercator projection
    gpsData = calcProjection(gpsData)

    # Move the projected data to the 0,0 origin of a cartesial coordinate system
    # and get the raw width and height of the resulting vector data
    gpsData, width, height = moveProjectedData(gpsData)

    # Write the resulting SVG data to the requested output file or STDOUT
    maxpx=min(3000,0.013*max(width,height))
    writeSvgData(gpsData, width, height, maxpx, None , 'input/output_track.svg')

if __name__ == '__main__':
    main()