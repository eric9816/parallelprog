import string
import time

letters = string.ascii_lowercase
eng_letters = list(letters + '_')
hw_lst = list('hello_world')
#hw_lst = list('zzzzzzzzzzzzzzzz')

result = ['' for _ in range(1, len(hw_lst) + 1)]
for idx, hw_letter in enumerate(hw_lst, 0):
    time.sleep(0.03)
    for eng_letter in eng_letters:
        result[idx] = eng_letter
        if eng_letter == hw_letter:
            time.sleep(0.03)
            break
        time.sleep(0.03)
        print(''.join(result))
print(''.join(result))


        # print(result)
        # if eng_letter == hw_letter:
        #     time.sleep(0.5)
        #     result += eng_letter
        #     break
