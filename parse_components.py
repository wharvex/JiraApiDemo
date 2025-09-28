import datetime

def parse_component_durations(changelog):
    history = changelog['values']
    durations = {}
    last_assigned_time = {}

    for item in history:
        created = item['created']  # e.g. "2025-09-27T12:34:56.789+0000"
        for change in item['items']:
            if change['field'] == 'components':
                # Component added
                if change['toString']:
                    for comp in change['toString'].split(','):
                        comp = comp.strip()
                        last_assigned_time[comp] = created
                # Component removed
                if change['fromString']:
                    for comp in change['fromString'].split(','):
                        comp = comp.strip()
                        if comp in last_assigned_time:
                            start = datetime.datetime.strptime(last_assigned_time[comp][:19], '%Y-%m-%dT%H:%M:%S')
                            end = datetime.datetime.strptime(created[:19], '%Y-%m-%dT%H:%M:%S')
                            delta = end - start
                            durations[comp] = durations.get(comp, datetime.timedelta()) + delta
                            del last_assigned_time[comp]
    return durations

# Example use:
# changelog = ... # as returned by the API
# print(parse_component_durations(changelog))