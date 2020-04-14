/*
* Author: suxSx
*
* Device Handler Button
*/

preferences {
    input "internal_ip", "text", title: "IP Addr:", required: false
    input "internal_port", "text", title: "Port (if not 80)", required: false
    input "internal_on_path", "text", title: "On Path (/function?q=this)", required: false
    input "internal_off_path", "text", title: "Off Path (/function?q=this)", required: false
}

metadata {
	definition (name: "WEB Service Switch", namespace: "python-api-request", author: "suxSx") {
		capability "Actuator"
			capability "Switch"
			capability "Sensor"
	}

	// simulator metadata
	simulator {
	}

	// UI tile definitions
	tiles {
		standardTile("button", "device.switch", width: 2, height: 2, canChangeIcon: true) {
			state "off", label: 'Off', action: "switch.on", icon: "st.switches.switch.off", backgroundColor: "#ffffff", nextState: "on"
				state "on", label: 'On', action: "switch.off", icon: "st.switches.switch.on", backgroundColor: "#79b821", nextState: "off"
		}
		standardTile("offButton", "device.button", width: 1, height: 1, canChangeIcon: true) {
			state "default", label: 'Force Off', action: "switch.off", icon: "st.switches.switch.off", backgroundColor: "#ffffff"
		}
		standardTile("onButton", "device.switch", width: 1, height: 1, canChangeIcon: true) {
			state "default", label: 'Force On', action: "switch.on", icon: "st.switches.switch.on", backgroundColor: "#79b821"
		}
		main "button"
			details (["button","onButton","offButton"])
	}
}

def parse(String description) {
	log.debug(description)
}

def on() {
    def port
        if (internal_port){
            port = "${internal_port}"
        } else {
            port = 80
        }

    def result = new physicalgraph.device.HubAction(
            method: "GET",
            path: "${internal_on_path}",
            headers: [
            HOST: "${internal_ip}:${port}"
            ]
            )

    sendHubCommand(result)
    sendEvent(name: "switch", value: "on") 
    log.debug "Executing ON" 
    log.debug result
}

def off() {
    def port
        if (internal_port){
            port = "${internal_port}"
        } else {
            port = 80
        }

    def result = new physicalgraph.device.HubAction(
            method: "GET",
            path: "${internal_off_path}",
            headers: [
            HOST: "${internal_ip}:${port}"
            ]
            )

    sendHubCommand(result)
    sendEvent(name: "switch", value: "off")
    log.debug "Executing OFF" 
    log.debug result
}