from src.reading import *
import re
import cmath
from datetime import datetime


def clean_lines(lines):
    valid_list = []
    for line in lines:
        # Start with !
        r = re.match("^[!\n\#]", line)
        if not r:
            valid_list.append(line.rstrip("\n"))
    return valid_list


def create_objects(path):
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    lines = clean_lines(lines)
    list_obj = []
    for line in lines:
        line = line.split()
        obj = Reading(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
        list_obj.append(obj)
    return list_obj


def get_b_ac(thru, line):
    # T2 * inv(T1)
    new_t_mat = line.t_mat * thru.t_mat_inv
    # Getting b (a = t21, b = t22-t11, c = -t12)
    a = new_t_mat[1][0]
    b = (new_t_mat[1][1]) - (new_t_mat[0][0])
    c = -(new_t_mat[0][1])
    # x = (-b + sqre(b**2-4*ac))/2
    sqre = cmath.sqrt((b * b) - (4 * a * c))
    x1 = (-b + sqre) / (2 * a)
    x2 = (-b - sqre) / (2 * a)
    if abs(x1) < abs(x2):
        b = x1
        ac = x2
    else:
        b = x2
        ac = x1
    return b, ac


def get_aest(b, w1, ca):
    # Gamma = 1
    aest = (b - w1)/((w1*ca)-1)
    return aest


def get_correct_dut(dut, thru, line, open):
    b, ac = get_b_ac(thru, line)
    # with t1 - g = t22, f = t21/g, e = t12/g, d = t11/g
    g = thru.t22
    f = thru.t21/g
    e = thru.t12/g
    d = thru.t11/g
    w1 = open.s11
    w2 = open.s22
    ca = 1/ac
    beta_alfa = (e-b)/(d - (b*f))
    fi = ((ac*f) - d)/(ac - e)
    # Getting a
    aest = get_aest(b, w1, ca)
    term_1 = (d - (b*f))*(b-w1)*(1 + (beta_alfa*w2))
    term_2 = (1 - (ca*e))*(fi+w2)*((ca*w1)-1)
    a_temp = cmath.sqrt(term_1/term_2)
    a1 = +a_temp
    a2 = -a_temp
    dif_a1 = aest - a1
    dif_a2 = aest - a2
    if abs(dif_a1) < abs(dif_a2):
        a = a1
    else:
        a = a2
    # Getting c
    c = a/ac
    # Getting alfa
    alfa = ((d-(b*f))/(1 - (ca*e)))/a
    # Getting beta
    beta = beta_alfa*alfa
    # Getting r22Ro22
    r22ro22 = (g*(ac-e))/(ac-b)
    # Getting S11
    term_1 = r22ro22*(a-(b*c))*(alfa-(beta*fi))*((alfa*dut.t12)-(beta*dut.t11)+(b*beta*dut.t21)-(b*alfa*dut.t22))
    term_2 = (c*beta*dut.t11)-(c*alfa*dut.t12)-(a*beta*dut.t21)+(a*alfa*dut.t22)
    s11 = term_1/term_2
    # Getting S22
    term_1 = r22ro22*(a-(b*c))*(alfa-beta*fi)*((c*fi*dut.s12)-(c*dut.t11)+(a*(dut.t21 - (fi*dut.t22))))
    term_2 = (c*beta*dut.t11)-(c*alfa*dut.t12)-(a*beta*dut.t21)+(a*alfa*dut.t22)
    s22 = term_1/term_2
    # Getting S21
    term_1 = r22ro22*(a-(b*c))*(alfa-(beta*fi))
    term_2 = (c*beta*dut.t11)-(c*alfa*dut.t12)-(a*beta*dut.t21)+(a*alfa*dut.t22)
    s21 = term_1/term_2
    # Getting S12
    sub_term_1 = r22ro22*(a - (b*c))*(alfa-(beta*fi))*(dut.t11 - (fi*dut.t12)-(b*dut.t21)+(b*fi*dut.t22))
    sub_term_2 = (c*beta*dut.t11)-(c*alfa*dut.t12)-(a*beta*dut.t21)+(a*alfa*dut.t22)
    term_1 = (sub_term_1/sub_term_2)+(s11*s22)
    term_2 = s21
    s12 = term_1/term_2
    return dut.frequency, s11, s21, s12, s22


dut_path = 'DUT.s2p'
thru_path = 'thru.s2p'
line_path = 'line.s2p'
open_path = 'Open.s2p'

dut_list = create_objects(dut_path)
thru_list = create_objects(thru_path)
line_list = create_objects(line_path)
open_list = create_objects(open_path)

# Creating text file
file = open("Correct.s2p", "w")
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
file.write("! Created on " + dt_string + "\n")
file.write("! CINVESTAV" + "\n\n")

file.write("! S-Parameter data\n")
file.write("! freq S11 S21 S12 S22\n")
file.write("# Hz S RI R 50\n")
for i in range(len(dut_list)):
    frequency, s11, s21, s12, s22 = get_correct_dut(dut_list[i], thru_list[i], line_list[i], open_list[i])
    file.write(str(frequency) + " " + "{:.15f}".format(s11.real) + " " + "{:.15f}".format(s11.imag) + " "
               + "{:.15f}".format(s21.real) + " " + "{:.15f}".format(s21.imag) + " "
               + "{:.15f}".format(s12.real) + " " + "{:.15f}".format(s12.imag) + " "
               + "{:.15f}".format(s22.real) + " " + "{:.15f}".format(s22.imag) + "\n")
file.close()





