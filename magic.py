import json
import uuid
# Load the Zabbix template example
template_path = "zbx_export_templates.json"
with open(template_path, 'r') as f:
    zabbix_template = json.load(f)

# Extract the items list from the Zabbix template
items_list = zabbix_template['zabbix_export']['templates'][0]['items']

# Define the ControlData JSON structure to Zabbix template mapping
control_data_list = [
    {"Attribute": "TI", "Type": "String", "Description": "Actual Timing in Voyager format AAAA-MM-GG HH:MM:SS", "Key": "voyager.status.ti"},
    {"Attribute": "TIUTC", "Type": "String", "Description": "UTC Timing in Voyager format AAAA-MM-GG HH:MM:SS", "Key": "voyager.status.tiutc"},
    {"Attribute": "VOYSTAT", "Type": "Integer", "Description": "Actual Status of Voyager Application", "Key": "voyager.status.voystat"},
    {"Attribute": "SETUPCONN", "Type": "Boolean", "Description": "Indicate if all setup controls in Voyager are connected with true or false", "Key": "voyager.status.setupconn"},
    {"Attribute": "CCDCONN", "Type": "Boolean", "Description": "Indicate if camera control is connected or not. True = connected. False if not connected or control is empty", "Key": "voyager.status.ccdconn"},
    {"Attribute": "CCDTEMP", "Type": "Number", "Description": "Temperature of cooling in Camera", "Key": "voyager.status.ccdtemp"},
    {"Attribute": "CCDPOW", "Type": "Number", "Description": "Percentage of power used by Peltier", "Key": "voyager.status.ccdpow"},
    {"Attribute": "CCDSETP", "Type": "Number", "Description": "Temperature Set Point asked to Cooler", "Key": "voyager.status.ccdsetp"},
    {"Attribute": "CCDCOOL", "Type": "Boolean", "Description": "True if Peltier is switched on or False if is switched off or Peltier is not present", "Key": "voyager.status.ccdcool"},
    {"Attribute": "CCDSTAT", "Type": "Integer", "Description": "Status of cooling automa inside Voyager", "Key": "voyager.status.ccdstat"},
    {"Attribute": "MNTCONN", "Type": "Boolean", "Description": "Indicate if mount control is connected or not. True = connected. False if not connected or control is empty", "Key": "voyager.status.mntconn"},
    {"Attribute": "MNTPARK", "Type": "Boolean", "Description": "Indicate if mount is parked. True = connected. False if not connected or control is empty", "Key": "voyager.status.mntpark"},
    {"Attribute": "MNTRA", "Type": "String", "Description": "Actual RA of Mount JNow", "Key": "voyager.status.mntra"},
    {"Attribute": "MNTDEC", "Type": "String", "Description": "Actual DEC of Mount JNow", "Key": "voyager.status.mntdec"},
    {"Attribute": "MNTRAJ2000", "Type": "String", "Description": "Actual RA of Mount J2000", "Key": "voyager.status.mntraj2000"},
    {"Attribute": "MNTDECJ2000", "Type": "String", "Description": "Actual DEC of Mount J2000", "Key": "voyager.status.mntdecj2000"},
    {"Attribute": "MNTAZ", "Type": "String", "Description": "Actual Azimuth of Mount", "Key": "voyager.status.mntaz"},
    {"Attribute": "MNTALT", "Type": "String", "Description": "Actual Altitude of Mount", "Key": "voyager.status.mntalt"},
    {"Attribute": "MNTPIER", "Type": "String", "Description": "Actual Pier of Mount (pierWest = Before Meridian, pierEast = After Meridian)", "Key": "voyager.status.mntpier"},
    {"Attribute": "MNTTFLIP", "Type": "String", "Description": "Time to Meridian Cross in HH:mm:SS if negative mean is before", "Key": "voyager.status.mnttflip"},
    {"Attribute": "MNTSFLIP", "Type": "Integer", "Description": "Status of Meridian Flip in Voyager", "Key": "voyager.status.mntsflip"},
    {"Attribute": "MNTTRACK", "Type": "Boolean", "Description": "Indicate if the mount is tracking", "Key": "voyager.status.mnttrack"},
    {"Attribute": "MNTSLEW", "Type": "Boolean", "Description": "Indicate if the mount is slewing", "Key": "voyager.status.mntslew"},
    {"Attribute": "AFCONN", "Type": "Boolean", "Description": "Indicate if Autofocus is connected. True = connected. False if not connected or control is empty", "Key": "voyager.status.afconn"},
    {"Attribute": "AFTEMP", "Type": "Numeric", "Description": "Temperature coming from Focuser. Some special value is possible", "Key": "voyager.status.aftemp"},
    {"Attribute": "AFPOS", "Type": "Numeric", "Description": "Position of Focuser in Step. Some special value is possible", "Key": "voyager.status.afpos"},
    {"Attribute": "SEQTOT", "Type": "Integer", "Description": "Total in seconds of all shot in a Sequence running", "Key": "voyager.status.seqtot"},
    {"Attribute": "SEQPARZ", "Type": "Integer", "Description": "Total in seconds of elapse shot in a Sequence Running", "Key": "voyager.status.seqparz"},
    {"Attribute": "GUIDECONN", "Type": "Boolean", "Description": "Indicate if guide controls is connected or not. True = connected. False if not connected or control is empty", "Key": "voyager.status.guideconn"},
    {"Attribute": "GUIDESTAT", "Type": "Integer", "Description": "Status of guide inside Voyager", "Key": "voyager.status.guidestat"},
    {"Attribute": "DITHSTAT", "Type": "Integer", "Description": "Status of Dithering inside Voyager", "Key": "voyager.status.dithstat"},
    {"Attribute": "GUIDEX", "Type": "Numeric", "Description": "Guide error in pixels in X axis", "Key": "voyager.status.guidex"},
    {"Attribute": "GUIDEY", "Type": "Numeric", "Description": "Guide error in pixels in Y axis", "Key": "voyager.status.guidey"},
    {"Attribute": "PLACONN", "Type": "Boolean", "Description": "Indicate if planetarium controls is connected or not. True = connected. False if not connected or control is empty", "Key": "voyager.status.placonn"},
    {"Attribute": "PSCONN", "Type": "Boolean", "Description": "Indicate if power supply is connected", "Key": "voyager.status.psconn"},
    {"Attribute": "SEQNAME", "Type": "String", "Description": "Name of Sequence running", "Key": "voyager.status.seqname"},
    {"Attribute": "SEQSTART", "Type": "String", "Description": "hh:mm:ss of sequence start", "Key": "voyager.status.seqstart"},
    {"Attribute": "SEQREMAIN", "Type": "String", "Description": "hh:mm:ss of remaining time to finish sequence", "Key": "voyager.status.seqremain"},
    {"Attribute": "SEQEND", "Type": "String", "Description": "hh:mm:ss of sequence end", "Key": "voyager.status.seqend"},
    {"Attribute": "RUNSEQ", "Type": "String", "Description": "FileName of actually running Sequence, empty if no Sequence running", "Key": "voyager.status.runseq"},
    {"Attribute": "RUNDS", "Type": "String", "Description": "FileName of actually running DragScript, empty if no DragScript running", "Key": "voyager.status.runds"},
    {"Attribute": "ROTCONN", "Type": "Boolean", "Description": "Indicate if rotator control is connected. True = connected. False if not connected or control is empty", "Key": "voyager.status.rotconn"},
    {"Attribute": "ROTPA", "Type": "Numeric", "Description": "Position Angle in Degree of the Rotator (-1 or ERROR VALUE mean unknown position)", "Key": "voyager.status.rotpa"},
    {"Attribute": "ROTSKYPA", "Type": "Numeric", "Description": "Last Position Angle of the camera in the SKY like resolved in solving actions (-1 or ERROR VALUE = unknown position)", "Key": "voyager.status.rotskypa"},
    {"Attribute": "ROTISROT", "Type": "Boolean", "Description": "Indicate if the rotator is rotating. True = is rotating", "Key": "voyager.status.rotisrot"},
    {"Attribute": "DOMECONN", "Type": "Boolean", "Description": "Indicate if dome control is connected. True = connected. False if not connected or control is empty", "Key": "voyager.status.domeconn"},
    {"Attribute": "DOMESHUTTER", "Type": "String", "Description": "Indicate the status of Shutter in ASCOM string representation", "Key": "voyager.status.domeshutter"},
    {"Attribute": "DOMEPA", "Type": "Numeric", "Description": "Position Angle in Degree of the Dome", "Key": "voyager.status.domepa"},
    {"Attribute": "DOMEISMOV", "Type": "Boolean", "Description": "Indicate if the dome is rotating or shutter is moving. True = is rotating/moving", "Key": "voyager.status.domeismov"}
]

def data_type_maps(ctype):
    if ctype == "String":
        return "TEXT"
    elif ctype == "Boolean":
        return "BINARY"
    elif ctype == "Number":
        return "FLOAT"
    elif ctype == "Numeric":
        return "FLOAT"
    elif ctype == "Integer":
        return "UNSIGNED"
    else:
        return "TEXT"
    

for item in control_data_list:
    new_item = {
        "uuid": uuid.uuid4().hex,
        "name": f"Control Data - {item['Attribute']}",
        "type": "DEPENDENT",
        "key": item["Key"],
        "delay": "0",
        "trends": "0",
        "value_type": data_type_maps(item["Type"]),
        "description": item["Description"],
        "preprocessing": [
            {
                "type": "JSONPATH",
                "parameters": [
                    f"$.{item['Attribute']}"
                ]
            }
        ],
        "master_item" : {
            "key" : 'restvas.run[GetControlData]'
        },
        "tags" : [
            {
                "tag": "description",
                "value": "Voyager"
            }
        ]
    }
    if item["Type"] == "Boolean":
        new_item["preprocessing"].append({
                                "type": "JAVASCRIPT",
                                "parameters": [
                                    "var b64 = btoa(value)\nreturn b64"
                                ]
                            })
        
    items_list.append(new_item)

# Save the updated template back to the file
with open('updated_zbx_export_templates.json', 'w') as file:
    json.dump(zabbix_template, file, indent=4)

# Display the updated Zabbix template to the user
# import ace_tools as tools; tools.display_dataframe_to_user("Updated Zabbix Template", pd.DataFrame(new_items))
