def get_outputs(input):
    outputs=[0, 0, 0, 0, 0]
    nums = [2, 3, 5, 7, 11]
    index = 0
    while index < len(nums):
        if input % nums[index] == 0:
            input = input // nums[index]
            outputs[index] += 1
        else:
            index += 1

    return outputs

count = int(input())
values = []
for i in range(0, count):
    values.append(int(input()))

for i in range(0, count):
    print(f"#{i + 1} {' '.join(map(str, get_outputs(values[i])))}")
    
