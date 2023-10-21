def main():
    nfs = input().split()
    n, f, s = nfs[0], nfs[1], nfs[2]
    course_iq = input().split()
    rob_iq = input().split()

    for i in range(len(course_iq)):
        course_iq[i] = [int(course_iq[i])]
    for i in range(int(n) - len(course_iq)):
        course_iq.append([0])
    for i in range(len(rob_iq)):
        rob_iq[i] = int(rob_iq[i])

    for i in rob_iq:
        sums = []
        for j in course_iq:
            if len(j) >= 2:
                sums.append((j[-1] + j[-2]) * len(j))
            else:
                sums.append(j[0] * len(j))
        min_num = min(sums)

        for j in range(len(course_iq)):
            if len(course_iq[j]) >= 2:
                num = (course_iq[j][-1] + course_iq[j][-2]) * len(course_iq[j])
            else:
                num = course_iq[j][0] * len(course_iq[j])
            if num == min_num:
                course_iq[j].append(i)
                print(j + 1, end=" ")
                break
    print()


if __name__ == "__main__":
    main()
