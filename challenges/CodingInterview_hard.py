# Create a function to check if a candidate is qualified in an imaginary coding interview of
# an imaginary tech startup.
#
# The criteria for a candidate to be qualified in the coding interview is:
#
# The candidate should have complete all the questions.
# The maximum time given to complete the interview is 120 minutes.
# The maximum time given for very easy questions is 5 minutes each.
# The maximum time given for easy questions is 10 minutes each.
# The maximum time given for medium questions is 15 minutes each.
# The maximum time given for hard questions is 20 minutes each.
# If all the above conditions are satisfied, return "qualified", else return "disqualified".
#
# You will be given a list of time taken by a candidate to solve a particular question
# and the total time taken by the candidate to complete the interview.
#
# Given a list , in a true condition will always be in the format [very easy, very easy,
# easy, easy, medium, medium, hard, hard].
#
# The maximum time to complete the interview includes a buffer time of 20 minutes.
def interview(lst, tot):
	if tot>120 or len(lst)<8:
		return "disqualified"
	if lst[0]>5 or lst[1]>5:
		return "disqualified"
	elif lst[2]>10 or lst[3]>10:
		return "disqualified"
	elif lst[4]>15 or lst[5]>15:
		return "disqualified"
	elif lst[6]>20 or lst[7]>20:
		return "disqualified"
	else:
		return "qualified"