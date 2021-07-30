from time import sleep
import pyperclip
import pyautogui
import random
import common
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import requests
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

class UserFacebook():
	def __init__(self):
		self.name = None
		self.username = None
		self.avata = None

	def compare(self,other):
		if other.name == self.name and other.username == self.username and other.avata == self.avata:
			return True
		return False

def spamBot():
	print('\nStep1: Enter your message, use || char to seperate each message\nStep2: Enter number of times you want to spam\nStep3: Enter delay time each message\nStep4: Focus the text box where you type the message')
	msg = input("\nEnter your message: ").split(" || ")
	n = int(input("Enter number of times: "))
	m = float(input("Enter delay time: "))

	print("Ready...")
	# countdown 5s
	for i in range(5, 0, -1):
		print(i, end="...", flush='False')
		sleep(1)
	print("Goooooo !")

	# SPAM
	for i in range(n):
		pyperclip.copy(random.choice(msg))
		pyautogui.hotkey("ctrl", "v")
		pyautogui.press("enter")
		sleep(m)  # Delay

def saveAllPhotos(self):

	friendName = input("\nEnter your friend name: ").strip()

	self.browser.get(url='https://facebook.com/'+friendName+'/photos_all')

	print('\nWait a minute, system is loading your photos ... \n')

	# Scrolldown to load all photos
	common.scrollDownToBottom(self.browser, 'document.body', True)

	wrapper = self.browser.find_element_by_xpath(
		"//div[@data-pagelet='ProfileAppSection_0']")

	# List A tag - List Video => Total Photos
	listA = wrapper.find_elements_by_xpath(
		"//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 datstx6m l9j0dhe7 k4urcfbm']")
	listVideo = wrapper.find_elements_by_xpath(
		"//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi knj5qynh ljqsnud1']")
	for i in range(len(listVideo)):
		listA.pop()

	i = 0
	count = 5 if 5 < len(listA) else len(listA)
	mainWindow = self.browser.current_window_handle

	print("Total: " + str(len(listA)) + ' photos\n')

	progressBar = tqdm(total=len(listA),
						desc='Progressing: ')  # Progress Bar
	while i < count:
		for j in range(i, count):
			# Open link in a new tab
			listA[j].send_keys(Keys.CONTROL + Keys.RETURN)

		tabs = self.browser.window_handles
		for index, tab in enumerate(tabs):  # 1 loop load only 5 pics
			if(index != 0):  # leave main tab
				self.browser.switch_to.window(tabs[index])

				try:
					picEle = self.wait.until(expected_conditions.visibility_of_element_located(
						(By.XPATH, "//img[@data-visualcompletion='media-vc-image'][@referrerpolicy='origin-when-cross-origin']")))
					# --- Save photo from pic URL ---
					response = requests.get(picEle.get_attribute('src'))
					with open('./public/'+str(i+1)+'.png', 'wb') as file:
						file.write(response.content)
					self.browser.close()
				except:
					pass
				i = i + 1

		# Switch to Main tab every loop
		self.browser.switch_to_window(mainWindow)

		if i == count:
			count = count + 5
		if count > len(listA):
			count = len(listA)
		progressBar.update(5)

	progressBar.close()
	print('\nAll done !!! See your photos at ./public/')

def photoAnalyze(self):
	def autolabel(rects,ax):
		"""Attach a text label above each bar in *rects*, displaying its height."""
		for i in range(len(rects)):
			height = rects[i].get_height()
			ax.annotate('{}'.format(height),
						xy=(rects[i].get_x() + rects[i].get_width() / 2, height),
						xytext=(0, 3),  # 3 points vertical offset
						textcoords="offset points",
						ha='center', va='bottom')

	def whoReactedTheMost(react_type,total_users,total_reactions):
		#like,love,haha,wow,dry,angry
		REACT = ["https://scontent.fcgh21-1.fna.fbcdn.net/m1/v/t6/An8JkpVv4NEzRagilLipZW9eAICo35S1A0gUa4zw4Kr53H6QUj1q7YbT6GS0zMJlLCmB4Wbxqu-bGVq1U-a3JrxL3l7S5zaUNIcxYJ4uUPCNDlXP.png?ccb=10-4&oh=842349c9832f86bd1eb138d06b897fdf&oe=61085118","https://scontent-lax3-1.xx.fbcdn.net/m1/v/t6/An9tU9mltzRvDoDeXQEJFl0TPMhk16ErJvLOtTBVW19D9Ks5FI_j6pZG-fFN3eJkOijusD5KWbb-YUjyv4WE1hCqkOc3spA_jeOHZBc-iWlwewzM.png?ccb=10-4&oh=f1bec64d19c56528c1498f0bc4303b90&oe=6108EB07&_nc_sid=55e238","https://scontent.fpbc2-1.fna.fbcdn.net/m1/v/t6/An-zv1qPExxz6a32zPrT6S6dY0H9YUfKQV5G2GtGfFkE-CFn00-Lq99Pp-0jUQwcEXXPxYjbZXZoE416bpzpqaYFNgTSXlvM4nCbmBfRzzGxNu8.png?ccb=10-4&oh=2f2ca914347542ab14e23fdcb948e9f8&oe=6109F6EB","https://scontent-gig2-1.xx.fbcdn.net/m1/v/t6/An__wcku2C9egUdf94a5F1z38LKlNYEI-g0uLs0fHp8P_O_BCnO_5G1eYl98T_oRrRvFt2TeJO9z7Kn2px0MJFqjvZsZw6gGAhzX1fLhIoNydmCt.png?ccb=10-4&oh=67bea0f90cbceb795a173a16f356cced&oe=6108EC51","https://scontent-dfw5-1.xx.fbcdn.net/m1/v/t6/An-ZyF_zEOJ1_yJh_zPGSRxDwnhaw3vaQPln0lvtl4k6fJF_2_6HxNmlcNxO7JOKGqiHT47T_WT9B7QsRpqJeDVvist1cde3YJ3mCMK0A6yjn-D-.png?ccb=10-4&oh=6f0fdf11e00296c36d05458c4a4b53fb&oe=6108AB32"]
		if react_type == "LIKE":
			react_type = REACT[0]
		elif react_type == "LOVE":
			react_type = REACT[1]
		elif react_type == "HAHA":
			react_type = REACT[2]
		elif react_type == "WOW":
			react_type = REACT[3]
		elif react_type == "DRY":
			react_type = REACT[4]

		list_users_by_react_type = []
		#filter users have react type match with input react type
		for i in range(len(total_reactions)):
			if total_reactions[i] == react_type:
				list_users_by_react_type.append(total_users[i])

		print(list_users_by_react_type)
		#count
		list_counted_users = []
		list_counted = []

		for i in range(len(list_users_by_react_type)):
			if len(list_counted_users) <= 0:
				list_counted_users.append(list_users_by_react_type[0])
			else:
				for j in range(len(list_counted_users)):
					flag = False
					if list_users_by_react_type[i].compare(list_counted_users[j]):
						flag = True
						break
				if flag == False:
					list_counted_users.append(list_users_by_react_type[i])

		for i in range(len(list_counted_users)):
			count = 0
			j = i
			for j in range(len(list_users_by_react_type)):
				if list_counted_users[i].compare(list_users_by_react_type[j]):
					count += 1
			list_counted.append(count)

		return top10(list_counted_users, list_counted)

	def whoInteractedTheMost(total_users,total_reactions):
		count_list = []
		user_list = []

		for i in range(len(total_users)):
			if len(user_list) == 0:
				flag = False
			else:
				for user in user_list:
					flag = False
					if total_users[i].compare(user):
						flag = True
						break
			if flag == False:
				user_list.append(total_users[i])
				count = 0
				j = i
				while j < len(total_users):
					if total_users[i].compare(total_users[j]):
						count += 1
					j += 1
				count_list.append(count)

		return top10(user_list, count_list)
	
	def top10(list_data,list_count):
		result_data = []
		result_count = []
		if len(list_data) > 10:
			total_loop = 10
		else:
			total_loop = len(list_data)
		for i in range(0,total_loop):
			max_value = list_count[0]
			index = 0
			for j in range(len(list_count)):
				if list_count[j] > max_value:
					max_value = list_count[j]
					index = j
			result_data.append(list_data[index])
			result_count.append(list_count[index])
			del list_count[index]
			del list_data[index]

		return result_data,result_count

	def converToCssElement(string):
		return "."+string.replace(" ",".")

	def openReactor(browser):
		list_reactors = []
		try:
			browser.find_element_by_css_selector(".bzsjyuwj.ni8dbmo4.stjgntxs.ltmttdrg.gjzvkazv").click()
		except:
			return list_reactors
		sleep(1)
		
		scroll_bar = "document.getElementsByClassName('kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc a8nywdso')[0]" #Get Javascript element
		scrollDownToBottom(browser, scroll_bar,False) #Scroll for load all reactors

		parents = browser.find_elements_by_css_selector(converToCssElement("ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j"))

		list_child = [elem.find_elements_by_tag_name("a") for elem in parents] #list Selector on each user
		list_child_clean = []
		for i in list_child:
			if len(i) != 0:
				list_child_clean.append(i)

		list_react_type = []
		for i in range(len(list_child_clean)):
			user = UserFacebook()
			user.name = list_child_clean[i][0].get_attribute("aria-label")
			user.avata = list_child_clean[i][0].find_element_by_tag_name("image").get_attribute("xlink:href")
			username_href = list_child_clean[i][1].get_attribute("href")
			user.username = username_href[25:len(username_href)-10]
			list_reactors.append(user)
			react_type = list_child_clean[i][0].find_element_by_tag_name("img").get_attribute("src")
			list_react_type.append(react_type)

		with open("data.txt",encoding="utf8",mode="a") as file:
			for i in range(len(list_reactors)):
				file.write(list_reactors[i].name+","+list_reactors[i].username+ ","+list_reactors[i].avata+","+list_react_type[i]+"\n")

		#close reactor
		browser.find_elements_by_css_selector(converToCssElement("oajrlxb2 tdjehn4e qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn s45kfl79 emlxlaya bkmhp75w spb7xbtv rt8b4zig n8ej3o3l agehan2d sk4xxmp2 taijpn5t tv7at329 thwo4zme"))[0].click() 

		return list_reactors

	def scrollDownToBottom(browser,elem,window=True):
		last_height = browser.execute_script("return "+elem+".scrollHeight") #Get first scroll height
		browser.execute_script(elem+".scrollTo(0,"+str(last_height)+");")
		while True:
			#Scroll down to bottom
			if window:
				browser.execute_script("window.scrollTo(0,"+str(last_height)+");")
			else:
				browser.execute_script(elem+".scrollTo(0,"+str(last_height)+");")

			#Wait to load
			sleep(1)

			# Calculate new scroll height and compare with last scroll height
			new_height = browser.execute_script("return "+elem+".scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height

	def menu(total_user,total_reactions,total_photos):
		
		table = [["Who reacted 'LIKE' the most",1],["Who reacted 'LOVE' the most",2],["Who reacted 'HAHA' the most",3],["Who reacted 'WOW' the most",4],["Who reacted 'DRY' the most",5],["Who reacted 'ANGRY' the most",6],["Who interacted the most",7],["Go back",0]]
		print("\n")
		for i in range(len(table)):
			print("[" + str(table[i][1]) + "] " + table[i][0])
		user_input = input("\nEnter your choice: ")
		while True:
			if user_input == "1":
				top10_user,top10_count = top10_user,top10_count = whoReactedTheMost("LIKE",total_user,total_reactions)
				break
			elif user_input == "2":
				top10_user,top10_count = whoReactedTheMost("LOVE",total_user,total_reactions)
				break
			elif user_input == "3":
				top10_user,top10_count = whoReactedTheMost("HAHA",total_user,total_reactions)
				break
			elif user_input == "4":
				top10_user,top10_count = whoReactedTheMost("WOW",total_user,total_reactions)
				break
			elif user_input == "5":
				top10_user,top10_count = whoReactedTheMost("DRY",total_user,total_reactions)
				break
			elif user_input == "6":
				top10_user,top10_count = whoReactedTheMost("ANGRY",total_user,total_reactions)
				break
			elif user_input == "7":
				top10_user,top10_count = whoInteractedTheMost(total_user, total_reactions)
				break
			elif user_input == "0":
				return
			else:
				print("Invalid input !!!")
				user_input = input("Enter your choice: ")

		header = ["Name","Photos"]
		table = []
		for i in range(len(top10_user)):
			temp = [top10_user[i].name,top10_count[i]]
			table.append(temp)
		print("\n"+tabulate(table,headers=header,tablefmt="grid"))

		labels = [elem.name for elem in top10_user]
		x = np.arange(len(labels))  # the label locations
		width = 0.35  # the width of the bars

		fig, ax = plt.subplots()
		fig.set_figwidth(18)
		rects1 = ax.bar(x, top10_count, width) 

		# Add some text for labels, title and custom x-axis tick labels, etc.
		ax.set_ylabel('Times')
		ax.set_ylim([0,total_photos])
		ax.set_xticks(x)
		ax.set_xticklabels(labels)	

		autolabel(rects1,ax)
		plt.show()
		return menu(total_user, total_reactions,total_photos)

	username = input("Enter your username you want to analyze: ")
	self.browser.get(url="https://facebook.com/" + username + "/photos")
	sleep(1) #Waiting load page

	#Scroll down for load all photos => Count how many photos do you have.
	scrollDownToBottom(self.browser,"document.body",True)
	self.browser.execute_script("window.scrollTo(0,0);") #Scroll window to top for click first photo
	total_photos = len(self.browser.find_elements_by_css_selector(converToCssElement("oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 datstx6m l9j0dhe7 k4urcfbm")))
	if total_photos == 0:
		print("User not found or User hasn't photo !!!")
		return self.getAllPhotos()
	print("Total photos = " + str(total_photos))
	input("Press ENTER to continue")
	sleep(1)
	try:
		self.browser.find_element_by_css_selector(converToCssElement("oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 datstx6m l9j0dhe7 k4urcfbm")).click() #Click first photo 
		sleep(2)
	except:
		print("NO PHOTO !!!")

	list_posts = []

	next_photo_btn = self.browser.find_elements_by_css_selector(converToCssElement("hu5pjgll lzf7d6o1"))[-1]

	percent = round(100/total_photos,2)
	for i in range(total_photos):
		list_posts.append(openReactor(self.browser))
		ActionChains(self.browser).move_to_element(next_photo_btn).perform() #hover to next_photo_btn
		processing = round(percent*(i+1),2)
		if processing > 100:
			print("-Completed-")
		else:
			print("Processing = "+str(processing)+"%")
		sleep(1)
		while True:
			try:
				next_photo_btn.click()
				break
			except:
				ActionChains(self.browser).move_to_element(next_photo_btn).perform() #hover to next_photo_btn
				sleep(1)

		with open("data.txt",encoding="utf8",mode="a") as file:
			file.write("======================\n")
		sleep(1)

	#Read file data.txt 
	with open("data.txt",encoding="utf8",mode="r") as file:
		read_file = file.read().split("======================")

	total_users = []
	total_reactions = []
	clean_user = []
	for post in read_file:
		post = post.split("\n")
		for user in post:
			user = user.split(",")
			if len(user) != 1:
				clean_user.append(user)
	for user in clean_user:
		fb_user = UserFacebook()
		fb_user.name, fb_user.username, fb_user.avata = user[0], user[1], user[2]
		total_users.append(fb_user)
		total_reactions.append(user[3])

	menu(total_users,total_reactions,len(read_file)-1)