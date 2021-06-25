from csv import reader

with open("/home/reda/catkin_ws/src/marker_test/bagfile/justbottle.csv") as csvfile:

	reader = reader(csvfile)
	lst = []
	lst_y = []
	lst_z = []

	for i in reader:
		lst.append(i[3])
		lst_y.append(i[4])
		lst_z.append(i[5])
	lst.pop(0)
	lst_y.pop(0)
	lst_z.pop(0)



def motion(lst):
	for x in range(0, len(lst), 2):
		initial_value = float(lst[x])
		final_value = float(lst[x+1])
		total = final_value - initial_value
		if abs(total) > 2:
			print(total)
			print("motion detected")
		else:
			print(total)
			print("no motion")

motion(lst)