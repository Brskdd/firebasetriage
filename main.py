import json

def prompt_questions():
    match_team_data = {}

    match_number = input("Enter Match Number: ")
    team_number = input("Enter Team Number: ")
    key = f"{match_number}_{team_number}"

    match_team_data[key] = {
        "Auton Amp": input("Auton Amp: "),
        "Auton Cross Line": input("Auton Cross Line (true/false): "),
        "Auton Speaker Made": input("Auton Speaker Made: "),
        "Auton Speaker Misses": input("Auton Speaker Misses: "),
        "Auton Start Pose": input("Auton Start Pose: "),
        "Endgame Climb Attempt": input("Endgame Climb Attempt (true/false): "),
        "Endgame Defended Against": input("Endgame Defended Against (true/false): "),
        "Endgame Defense Time": input("Endgame Defense Time: "),
        "Endgame End Pose": input("Endgame End Pose: "),
        "Endgame Time To Climb": input("Endgame Time To Climb: "),
        "Endgame Trap Note": input("Endgame Trap Note (true/false): "),
        "Match Number": match_number,
        "Notes": input("Notes: "),
        "Team Number": team_number,
        "Teleop Amps": input("Teleop Amps: "),
        "Teleop Preferred Shooting Pose": input("Teleop Preferred Shooting Pose: "),
        "Teleop Speaker Made": input("Teleop Speaker Made: "),
        "Teleop Speaker Misses": input("Teleop Speaker Misses: "),
    }

    return match_team_data

def main():
    data_list = []

    # Prompt questions multiple times
    while True:
        data_list.append(prompt_questions())

        add_more = input("Do you want to add more data? (yes/no): ").lower()
        if add_more != "yes":
            break

    # Write data to a file
    with open("data.json", "w") as f:
        json.dump(data_list, f, indent=4)

    print("Data has been written to data.json")

if __name__ == "__main__":
    main()