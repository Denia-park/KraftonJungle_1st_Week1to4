def bm_match(txt, pattern):
    """
    보이어 무어법으로 문자열 검색
    """
    skip = [None] * 256  # 건너뛰기 표

    # 건너뛰기 표 만들기
    for pt in range(256):  # pattern의 길이로 초기화
        skip[pt] = len(pattern)

    for pt in range(len(pattern)):
        skip[ord(pattern[pt])] = len(pattern) - pt - 1

    # 검색하기
    while pt < len(txt):
        pp = len(pattern) - 1
        while txt[pt] == pattern[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += (
            skip[ord(txt[pt])]
            if skip[ord(txt[pt])] > len(pattern) - pp
            else len(pattern) - pp
        )

    return -1


txt = input("텍스트를 입력하세요.: ")  # 텍스트용 문자열
pattern = input("패턴을 입력하세요.: ")  # 패턴용 문자열

idx = bm_match(txt, pattern)  # 문자열 s1 ~ s2를 보이어·무어법 으로 검색

if idx == -1:
    print("텍스트 안에 패턴이 존재하지 않습니다.")
else:
    print(f"{(idx + 1)}번째 문자가 일치합니다.")
