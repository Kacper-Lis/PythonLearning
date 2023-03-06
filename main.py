from patient import Patient

patient_list = [['Imie1', 'nazw1', '23', 'M', 'Rak'],
                ['Imie2', 'nazw2', '23', 'M', 'Rak'],
                ['Imie3', 'nazw3', '22', 'M', 'Wylew']]
# 2d-array [0,1,2]

patient_dict = {'imie1': ['Imie1', 'nazw1', '23', 'M', 'Rak'],
                'imie2': ['23', 'Imie2', 'Imie', 'Rak', 'F'],
                'imie3': ['Imie3', 'nazw2', '22', 'M', 'Wylew']}

patient1 = Patient('Bob', 'Smith', 18, 'M')
patient2 = Patient('Rob', 'Smith', 24, 'M')
patient3 = Patient('Jess', 'Smith', 60, 'F')

print(patient1.first_name)
print(patient3.full_name)

print(patient1)
patient_obj_list = [patient1, patient2, patient3]
print(patient_obj_list)

print('Patient class method')
print(patient1.is_family(patient2))
# Can we do better


def is_family(pat1, pat2):
    return pat1.last_name == pat2.last_name


print('Random method')
print(is_family(patient1, patient2))


def transform_int(i):
    return i ** 2


def transform_list(array):
    array[0] = array[0] * array[0]
    return array


num = 5
new_num = transform_int(num)
# print(new_num)
# print(num)

arr = [5, 2, 3]
new_arr = transform_list(arr)
# print(new_arr)
# print(arr)


new_arr[0] = 5
# print(arr)
# arr[0] = 10
# print(new_arr)



def transform_string(s):
    return s + 'huj'


s1 = 'twoj'
s2 = transform_string(s1)
# print(s1)
# print(s2)


# int -1 0 1 2 3 4
# bool
# float 0.1 .02
# str
