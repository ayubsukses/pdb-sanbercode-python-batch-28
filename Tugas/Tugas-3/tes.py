# # # europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
# # #           'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
# # #           'australia':'vienna' }

# # # # ubah ibukota German ke Berlin

# # # # europe['germany'] = 'berlin'
# # # # europe.pop('australia')
# # # # print(europe)

# # # country = { 
# # #            'spain': { 'capital':'madrid', 'population':46.77 },
# # #            'france': { 'capital':'paris', 'population':66.03 },
# # #            'germany': { 'capital':'berlin', 'population':80.62 },
# # #            'norway': { 'capital':'oslo', 'population':5.084 } 
# # #          }


# # # # print(country['germany']['population'])

# # # # country['indonesia'] =  {'capital' : 'jakarta', 'population' : 250}
# # # # print(country)

# # country = { 
# #            'spain': { 'capital':'madrid', 'population':46.77 },
# #            'france': { 'capital':'paris', 'population':66.03 },
# #            'germany': { 'capital':'berlin', 'population':80.62 },
# #            'norway': { 'capital':'oslo', 'population':5.084 },
# #            'indonesia' : {'capital':'jakarta', 'population':250}
# #          }

# # for key, value in country.items():
# #     print('Ibukota '+key+' adalah ' + key)

# obj_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]
# obj_list.discard(5, 9)
# print(obj_list)

set_1 = {1, 2, 3, 4, 5}
set_1.update([6, 7, 8])
set_1.remove(8)
print(set_1)