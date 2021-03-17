var fs = require("fs");

function read_file(filepath) {
    let text = fs.readFileSync(filepath)
        .toString()
        .trim()
        .split("\n")

    return text;
}

//----------------------part1-----------------------
// funktion gibt die richtung nach einer drehung zurück
function change_direction(previous_direction, input) {
    var direction_dict = {
        "E" : [0],
        "N" : [270, -90],
        "W" : [180, -180],
        "S" : [90, -270]
    }
    if (input.substring(0,1) == "R") { // nur der nullte bis (exklusive) dem ersten
        var direction = direction_dict[previous_direction][0];
        direction += parseInt(input.substring(1)); // alle ausser der erste im string
        var modulo = direction % 360;
        for (var key in direction_dict) {
            if (direction_dict[key].includes(modulo) === true) {
                return key
            }
        }

    }
    else if (input.substring(0,1) == "L") {
        var direction = direction_dict[previous_direction][0];
        direction -= parseInt(input.substring(1));
        var modulo = direction % 360;
        for (var key in direction_dict) {
            if (direction_dict[key].includes(modulo) === true) {
                return key
            }
        }
    }
}

function manhattan_dist(data) {
    var direction = "E";
    var x_position = 0;
    var y_position = 0;
    for (x in data) {
        if (data[x].substring(0,1) == "N") { // das boot fährt seitwärts usw.
            y_position += parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "S") {
            y_position -= parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "E") {
            x_position += parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "W") {
            x_position -= parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "R" || data[x].substring(0,1) == "L") { // das boot wechselt seine richtung
            direction = change_direction(direction, data[x]);
            console.log(direction);
        }
        else if (data[x].substring(0,1) == "F") { // das boot fährt geradeaus
            if (direction == "E") {
                x_position += parseInt(data[x].substring(1));
            }
            else if (direction == "W") {
                x_position -= parseInt(data[x].substring(1));
            }
            else if (direction == "N") {
                y_position += parseInt(data[x].substring(1));
            }
            else if (direction == "S") {
                y_position -= parseInt(data[x].substring(1));
            }
        }
    }
    return Math.abs(x_position) + Math.abs(y_position);
}

//----------------------part2-----------------------
// waypoint function
function change_waypoint(waypoint_start, input) {
    if (input.substring(0,1) == "R" && input.substring(1) == 90 || input.substring(0,1) == "L" && input.substring(1) == 270) {
        var new_waypoint = [waypoint_start[1], -waypoint_start[0]];
        return new_waypoint;
    }
    else if (input.substring(0,1) == "R" && input.substring(1) == 180 || input.substring(0,1) == "L" && input.substring(1) == 180) {
        var new_waypoint = [-waypoint_start[0], -waypoint_start[1]];
        return new_waypoint;
    }
    else if (input.substring(0,1) == "R" && input.substring(1) == 270 || input.substring(0,1) == "L" && input.substring(1) == 90) {
        var new_waypoint = [-waypoint_start[1], waypoint_start[0]];
        return new_waypoint;
    }
    else if (input.substring(0,1) == "N") {
        var new_waypoint = [waypoint_start[0], waypoint_start[1] + parseInt(input.substring(1))];
        return new_waypoint;
    }
    else if (input.substring(0,1) == "S") {
        var new_waypoint = [waypoint_start[0], waypoint_start[1] - parseInt(input.substring(1))];
        return new_waypoint;
    }
    else if (input.substring(0,1) == "E") {
        var new_waypoint = [waypoint_start[0] + parseInt(input.substring(1)), waypoint_start[1]];
        return new_waypoint;
    }
    else if (input.substring(0,1) == "W") {
        var new_waypoint = [waypoint_start[0] - parseInt(input.substring(1)), waypoint_start[1]];
        return new_waypoint;
    }
    
}

function manhattan_dist_waypoint(data, waypoint, starting_position) {
    for (x in data) {
        if (data[x].substring(0,1) == "F") { // schiffsposition ändert sich
            starting_position = [starting_position[0] + parseInt(data[x].substring(1))*waypoint[0], starting_position[1] + parseInt(data[x].substring(1))*waypoint[1]];
        }
        else {
            waypoint = change_waypoint(waypoint, data[x]) // wegpunkt ändert sich
        }
    }
    return Math.abs(starting_position[0]) + Math.abs(starting_position[1]);
}

function main() {
    var data = read_file("advent_of_code_12.txt");
//----------------------part1-----------------------
    // console.log(manhattan_dist(data));
//----------------------part2-----------------------
    var waypoint_start = [10, 1]; // wo der wegpunkt startet
    var starting_position = [0, 0]; // wo das schiff startet
    console.log(manhattan_dist_waypoint(data, waypoint_start, starting_position))
}

main();