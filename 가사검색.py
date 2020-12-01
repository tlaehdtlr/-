def solution(words, queries):
    word_dic = {}
    for w in words:
        if len(w) in word_dic:
            word_dic[len(w)]['count'] += 1
        else:
            word_dic[len(w)] = {}
            word_dic[len(w)]['count'] = 1
        tmp_dic = word_dic[len(w)]
        while w:
            if w[0] in tmp_dic:
                tmp_dic[w[0]]['count'] += 1
            else:
                tmp_dic[w[0]] = {}
                tmp_dic[w[0]]['count'] = 1
            tmp_dic = tmp_dic[w[0]]
            w = w[1:]
    reverse_word_dic = {}
    for w in words:
        if len(w) in reverse_word_dic:
            reverse_word_dic[len(w)]['count'] += 1
        else:
            reverse_word_dic[len(w)] = {}
            reverse_word_dic[len(w)]['count'] = 1
        tmp_dic = reverse_word_dic[len(w)]
        w = w[::-1]
        while w:
            if w[0] in tmp_dic:
                tmp_dic[w[0]]['count'] += 1
            else:
                tmp_dic[w[0]] = {}
                tmp_dic[w[0]]['count'] = 1
            tmp_dic = tmp_dic[w[0]]
            w = w[1:]

    answer = []
    for q in queries:
        match_dic = word_dic
        if q.startswith('?'):
            q = q[::-1]
            match_dic = reverse_word_dic
        if len(q) in match_dic:
            count = 0
            match_dic = match_dic[len(q)]
            while q:
                if q[0] == '?':
                    count = match_dic['count']
                    break
                elif q[0] not in match_dic:
                    break
                match_dic = match_dic[q[0]]
                q = q[1:]
        else:
            count = 0
        answer.append(count)
    return answer