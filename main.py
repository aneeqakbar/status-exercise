STATUSES = [
  "Requested",
  "Missing info",
  "Processed",
  "Activated",
  "Canceled"
]

def main(subtask_statuses):
  """
  Recieves an array of statuses and gives the general task status
  """
  general_task_status = "Requested"
  statuses_set = set(subtask_statuses)

  if len(statuses_set) == 1:
    general_task_status = subtask_statuses[0]
  elif STATUSES[1] in subtask_statuses:
    general_task_status = STATUSES[1]
  elif STATUSES[2] in subtask_statuses:
    general_task_status = STATUSES[2]
  elif len(statuses_set) == 2 \
    and (STATUSES[3]  in statuses_set \
    or STATUSES[4]  in statuses_set):
      general_task_status = STATUSES[3]

  return general_task_status

print(main([
  "Requested",
  "Requested",
  "Requested",
]))

print(main([
  "Activated",
  "Activated",
  "Canceled"
]))

print(main([
  "Requested",
  "Processed",
  "Canceled"
]))

print(main([
  "Processed",
  "Missing info",
  "Processed"
]))