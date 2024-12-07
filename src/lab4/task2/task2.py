import sys

def read_respondents_until_end():
    respondents = []
    input_str = input()
    while input_str != 'END':
        respondents.append(input_str.split(','))
        input_str = input()
    return respondents


def make_dict_with_groups(input_groups):
    groups = {}
    groups[(0, int(input_groups[0]))] = []
    for i in range(1, len(input_groups)):
        left = int(input_groups[i - 1]) + 1
        right = int(input_groups[i])
        groups[(left, right)] = []
    groups[(int(input_groups[-1]) + 1, 123)] = []
    return groups


class Group:
    def __init__(self, dict_group, respondents):
        self.dict_group = dict_group
        self.respondents = respondents

    def sort_dict_group(self):
        for key, value in self.dict_group.items():
            self.dict_group[key] = sorted(value, key=lambda x: (-x[1], x[0]))
        self.dict_group = dict(sorted(self.dict_group.items(), key=lambda item: item[0], reverse=True))

    def get_formatted_dict_group(self):
        res = ''
        self.sort_dict_group()
        dict_ = self.dict_group
        for key in dict_.keys():
            if len(dict_[key]) == 0:
                continue
            res += f'{key[0]}-{key[1]}: '
            for value in dict_[key]:
                if dict_[key][-1] == value:
                    res += f'{value[0]} ({value[1]})'
                else:
                    res += f'{value[0]} ({value[1]}), '
            res += '\n'
        return res

    def paste_into_groups(self):
        for i in range(len(self.respondents)):
            for key in self.dict_group.keys():
                if key[0] <= int(self.respondents[i][1]) <= key[1]:
                    self.dict_group[key].append((self.respondents[i][0], int(self.respondents[i][1])))


if __name__ == '__main__':
    groups = sys.argv[1:]
    respondents_ = read_respondents_until_end()
    dict_group_ = make_dict_with_groups(groups)
    obj = Group(dict_group_, respondents_)
    obj.paste_into_groups()
    print(obj.get_formatted_dict_group())
