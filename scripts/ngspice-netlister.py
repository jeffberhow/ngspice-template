#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET

# List of all SPICE elements
spice_passive_list=['R', 'L', 'C',]
spice_active_list=['D', 'Q', 'M']
spice_source_list=['V', 'I']
spice_subckt_list=['X']
spice_xspice_list=['A']

# User made
spice_test_list=['Z']
spice_probe_list=['P']

input_file=sys.argv[1]
output_file=sys.argv[2]

tree=ET.parse(input_file)
root=tree.getroot()

# The design section holds information like:
#       * schematic source path
#       * date of creation and Eeschema version
design=root[0]
# The components section holds component information like:
#       * component reference : comp.get('ref')
#       * component value : comp.find('value').text
#       * component fields : comp.find('fields')
components=root[1]
# The libparts section holds information like:
#       * library that the component is in
#       * pin numbers and types
#       * component descriptions, docs and footprints
libparts=root[2]
# The libraries section holds information like:
#       * Path to libraries
libraries=root[3]
# The nets section holds information like:
#       * What components to which net is connected
#       * The net "code" and net name
nets=root[4]

ofh=open(output_file, "w")

ofh.write(".title SPICE netlist generated by ngspice netlister\n")

ofh.write(".end\n")

ofh.close()
