from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  min = array[0]
  min_ind = 0
  for i in range(size):
    if min <= array[i]:
      min = array[i]
      min_ind = i
    temp = array[i]
    array[i] = array[min_ind]
    array[min_ind] = temp
  
  return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
