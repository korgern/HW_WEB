# Корабейник Илья Андреевич ФИТ-221
import numpy as np 

switch = int(input('Input global task: '))
match switch:
    case 1:
        switch_task = int(input('Input fist task: '))
        match switch_task:
            case 1:
                arr1 = np.array([1, 7, 13, 105])
                
                print("Размер памяти, занимаемый массивом: ", arr1.nbytes)
                np.savetxt('1st_task.txt', arr1)
                np.save('1st_task_byte.npy', arr1)
                loaded_arr1 = np.load('1st_task_byte.npy')
                print("Загруженный массив из бинарного файла: ", loaded_arr1)
                loaded_arr1 = np.loadtxt('1st_task.txt')
                print("Загруженный массив из текстового файла: ", loaded_arr1)
                
            case 2:
                arr21 = np.zeros(10)
                arr22 = np.ones(10)
                arr23 = np.full((1, 10), 5)

                print(arr21)
                print(arr22)
                print(arr23)
            case 3:                    
                arr3 = np.arange(30, 70, 2)
                print(arr3)
            case 4:
                
                arr4 = np.linspace(5, 50, 10)
                print(arr4)
            case 5:
                arr5 = np.random.randint(1, 100, size=(3, 3, 3))
                print(arr5)
            case 6:
                arr6 = np.arange(30, 42).reshape(3, 4)
                print(arr6)
            case 7:
                arr7 = np.linspace(1, 0, 100).reshape(10, 10)
                print(arr7)

            case 8:
                arr8 = np.diag(np.arange(1, 6))
                print(arr8) 
            case 9:
                arr9 = np.zeros(16).reshape(4, 4)
                arr9[1::2, ::2] = 1
                arr9[::2, 1::2] = 1
                print(arr9)
            case 10:
                arr10 = np.arange('2017-03-01', '2017-04-01', dtype='datetime64[D]')
                print(arr10)
                
    case 2:
        switch_task_2 = int(input('Input second task: '))
        match switch_task_2:
            case 1:
                
                arr1 = np.array([0, 10, 20, 40, 60])
                arr2 = np.array([10, 30, 40])
                common_elements = np.intersect1d(arr1, arr2)
                print(common_elements)
                
            case 2:
                arr = np.array([10, 10, 20, 20, 30, 30])
                unique_elements = np.unique(arr)
                print(unique_elements)
                
                arr1 = np.array([[1, 1], [2, 3]])
                unique_elements1 = np.unique(arr1)
                print(unique_elements1)  
            
            case 3:
                arr = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
                unique_elements, frequencies = np.unique(arr, return_counts=True)
                print("Уникальные элементы: ", unique_elements)
                print("Частоты элементов: ", frequencies)
            
            case 4: 
                arr = np.array([1, 2, 3, 4])
                repeated_arr = np.tile(arr, 2)
                print("Оригинальный массив: ", arr)
                print("Повторенный массив: ", repeated_arr)
                repeated_arr1 = np.tile(repeated_arr, 2)
                print("Дважды повторённый массив: ", repeated_arr1)
            
    #         case 5:
                
    # # case 3:
