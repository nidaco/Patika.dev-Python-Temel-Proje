"""
1-Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi,
non-scalar verilerden de oluşabilir.
Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""
def flatten(lst):
    flattened_list = []
    for element in lst:
        if isinstance(element, list):
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)
    return flattened_list
"""
Öncelikle verilen liste içindeki her bir eleman için döngü oluşturur.
Daha sonra, elemanın liste türünde olup olmadığını kontrol eder.
Eğer eleman liste ise, bu elemanın içindeki tüm elemanları düzleştirir ve flattened_list listesine ekler.
Eğer eleman liste değilse, elemanı flattened_list listesine ekler. 
Döngü bittikten sonra, flattened_list listesi döndürülür.
"""
"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""
def reverse_list(lst):
    if isinstance(lst, list):
        return [reverse_list(x) for x in reversed(lst)]
    return lst
"""
List comprehension, bir liste oluşturmak için kullanılan bir yapıdır ve genellikle for döngüsüyle birlikte kullanılır. 
34. satırda, reversed fonksiyonu ile lst listesi tersine çevrilir ve daha sonra bu tersine çevrilmiş liste üzerinde bir for döngüsü geçirilir. 
Bu döngü, her bir eleman için reverse_list fonksiyonunu çağırır ve bu fonksiyonun döndürdüğü değerleri bir liste oluşturur. 
Bu liste comprehension yapısının sonucu olarak geri döndürülür.
"""
