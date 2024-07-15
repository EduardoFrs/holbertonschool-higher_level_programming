#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template is not a string")

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Attendees is not a list of dictionaries")

    if not template:
        raise ValueError("Template is empty, no output files generated.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    for i, attendee in enumerate(attendees, start=1):
        invitation = template.replace('{name}', attendee.get('name', 'N/A'))
        invitation = invitation.replace('{event_title}', attendee.get('event_title', 'N/A'))
        invitation = invitation.replace('{event_date}', str(attendee.get('event_date', 'N/A')))
        invitation = invitation.replace('{event_location}', attendee.get('event_location', 'N/A'))

        output_filename = f'output_{i}.txt'

        if os.path.exists(output_filename):
            raise FileExistsError(f"File '{output_filename}' already exist")

        with open(output_filename, 'w') as f:
            f.write(invitation)
