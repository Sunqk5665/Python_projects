# str_a = 'foshajbcpudejlfg'
# str_b = 'fishabcdefg'
# cell = [[0 for j in range(len(str_a)+1)] for i in range(len(str_b)+1)]
#
# for j in range(1,len(str_a)+1):
#     for i in range(1,len(str_b)+1):
#         if str_a[j-1]==str_b[i-1]:
#             cell[i][j] = cell[i-1][j-1]+1
#         else:
#             cell[i][j] = max(cell[i-1][j],cell[i][j-1])
# max_List = []
# for li in cell:
#     max_List.append(max(li))
# print(max(max_List))