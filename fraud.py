import ipinfo
import geopy
from geopy import distance
from geopy.distance import vincenty

def score_IP():

    access_token = 'ffccd613ba24e5'
    handler = ipinfo.getHandler(access_token)
    new_ip = input("Enter a new IP address: ")
    details = handler.getDetails(new_ip)
    loc = details.loc
    split_loc = loc.split(",")

    #print(details.city)

    # replace with actual path to file
    file = open("/Users/henryjacobs/PycharmProjects/fraud/login_attempts.txt", "r")

    #dict that maps IP addresses to type of login, LOGIN or FRAUD
    ip_dict = {}

    for line in file:
        cur_item = line
        split_item = cur_item.split() # split the line in the file on whitespace
        ip_dict[split_item[1]] = split_item[0] # set key of dict to IP address (second el of split_Item) and the value
                                                # to the type of login (first el of split_Item)
    file.close

    min_dist = float("inf")
    score = 0.0
    for ip in ip_dict:
        cur_IP_Details = handler.getDetails(ip) # get ip info
        cur_IP_loc = cur_IP_Details.loc # get loc
        cur_split_loc = cur_IP_loc.split(",") #split loc into two strings
        cur_dist = calc_distance(cur_split_loc, split_loc) # distance between input location and cur_dist

        # update vars to keep track of the smallest distance between IPs in file and new IP to be scored
        if cur_dist < min_dist:
            min_dist = cur_dist
            score = cur_dist
            closest_ip = ip

    # check if closest IP address to new IP address was fraudulent
    if ip_dict[closest_ip] == "FRAUD":
        score += score # double score if fraudulent
        print("The login attempt coming from IP: " + ip + " is likely fraudulent with a score: " + str(score))
    else:
        print("The login attempt coming from IP: " + ip + " is NOT fraudulent with a score: " + str(score))

    return score

def calc_distance(lat_long_start, lat_long_end): # passed as list

    # converts elements of lists passed in to floats, then converts lists to tuples
    coords_1 = tuple([float(i) for i in lat_long_start])
    coords_2 = tuple([float(i) for i in lat_long_end])

    return geopy.distance.distance(coords_1, coords_2).miles

def main():
    score_IP()

if __name__ == "__main__": main()