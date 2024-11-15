"""MQTT Commands"""
CHAMBER_LIGHT_ON = {
    "system": {"sequence_id": "0", "command": "ledctrl", "led_node": "chamber_light", "led_mode": "on",
               "led_on_time": 500, "led_off_time": 500, "loop_times": 0, "interval_time": 0}}
CHAMBER_LIGHT_OFF = {
    "system": {"sequence_id": "0", "command": "ledctrl", "led_node": "chamber_light", "led_mode": "off",
               "led_on_time": 500, "led_off_time": 500, "loop_times": 0, "interval_time": 0}}

SPEED_PROFILE_TEMPLATE = {"print": {"sequence_id": "0", "command": "print_speed", "param": ""}}

GET_VERSION = {"info": {"sequence_id": "0", "command": "get_version"}}

PAUSE = {"print": {"sequence_id": "0", "command": "pause"}}
RESUME = {"print": {"sequence_id": "0", "command": "resume"}}
STOP = {"print": {"sequence_id": "0", "command": "stop"}}

PUSH_ALL = {"pushing": {"sequence_id": "0", "command": "pushall"}}

START_PUSH = { "pushing": {"sequence_id": "0", "command": "start"}}

SEND_GCODE_TEMPLATE = {"print": {"sequence_id": "0", "command": "gcode_line", "param": ""}} # param = GCODE_EACH_LINE_SEPARATED_BY_\n

# X1 only currently
GET_ACCESSORIES = {"system": {"sequence_id": "0", "command": "get_accessories", "accessory_type": "none"}}

CHANGE_FILAMENT_TEMPLATE = {
    "print": {
        "sequence_id": "2070",
        "command": "ams_filament_setting",
        "ams_id": 255,  # 255 is external spool, ams id 0-N for an AMS
        "tray_id": 254,  # 254 is external spool here, 0-3 for an AMS
        "tray_info_idx": "",  # one of the predefined codes in the slicer. This is mandatory
        "tray_color": "00000000",
        "nozzle_temp_min": 190,
        "nozzle_temp_max": 280,
        "tray_type": "",
        "setting_id": "",
        "reason": "success",
        "result": "success",
    }
}