def get_grades():
    return [5, 4, "3", 2, 1]


def calculate_average(grades):
    return sum(grades) / len(grades)

def clean_grades(grades):
    cleaned = []
    for g in grades:
        try:
            g_int = int(g)
            if 1 <= g_int <= 5:
                cleaned.append(g_int)
            else:
                print(f"Pomijam ocenę spoza zakresu: {g}")
        except (ValueError, TypeError):
            print(f"Niepoprawna ocena: {g}")
    return cleaned


def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"


def show_result():
    raw_grades= get_grades()
    grades = clean_grades(raw_grades)
    avg = calculate_average(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")

# add clean_grades function to remove all grades out of 1..5 scope