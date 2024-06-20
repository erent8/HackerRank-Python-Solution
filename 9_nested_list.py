if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):  # Öğrenci sayısını al
        name = input()             # Öğrencinin adını al
        score = float(input())     # Öğrencinin notunu al
        students.append([name, score])  # İsmi ve notu bir liste olarak ekle
    
    # Benzersiz notları ayıklama ve sıralama
    scores = sorted(set([score for name, score in students]))
    second_lowest_score = scores[1]
    
    # İkinci en düşük nota sahip öğrencilerin isimlerini toplama
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    
    # İsimleri alfabetik olarak sıralama
    second_lowest_students.sort()
    
    # Sonuçları yazdırma
    for student in second_lowest_students:
        print(student)

## KOD SATIRLARINI SİLMEYİ UNUTMAYIN
