# find nth highist keyvalue pair in a dictionary

# def nth_max(dict,n):
#
#     vals = list(dict.values())
#     sort_vals = sorted(set(vals), reverse=True)
#     nth_val = sort_vals[n-1]
#     print(nth_val)
#     nth_keys =[]
#     for k,v in dict.items():
#         if v == nth_val:
#             nth_keys.append(k)
#     return({min(nth_keys):nth_val})


def nth_max(dict,n):
    vals = list(dict.values())
    vals_sorted = sorted(set(vals), reverse =True)
    nth_max = vals_sorted[n-1]
    nth_kys = []
    for k,v in dict.items():
        if v == nth_max:
            nth_kys.append(k)
    return {min(nth_kys):nth_max}





print(nth_max({1:2, 2:3, 3:3, 4:3, 5:5},2))