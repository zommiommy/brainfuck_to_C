

tab_size = 4 #if you change this you are an horrible person

header = """
#define INFINITELY_LARGE_SIZE 8000
#include <stdio.h>
char array[INFINITELY_LARGE_SIZE] = {0};
char *ptr=array;
int main(){
%s
}
"""
in_string = input()
clustered_string = ""
out_string = ""

indent = 1

#clustering
current_command = ""
contatore = 0
for char in in_string:
	if char in ".,[]":
		clustered_string += str(contatore) + current_command
		clustered_string += "1" + char
		current_command = ""
		contatore = 0
	else:
		if char == current_command:
			contatore += 1
		else:
			clustered_string += str(contatore) + current_command
			current_command = char
			contatore = 1

clustered_string = clustered_string.replace("","")

#translating
digi = ""
for char in clustered_string:
	if char.isdigit():
		digi += char
	else:
		numero = int(digi)
		if char == '>':
			out_string += " " * indent * tab_size  + "ptr += %d;\n"%numero
		elif char == '<':
			out_string += " " * indent * tab_size  + "ptr -= %d;\n"%numero
		elif char == '+':
			out_string += " " * indent * tab_size  + "*ptr += %d;\n"%numero
		elif char == '-':
			out_string += " " * indent * tab_size  + "*ptr -= %d;\n"%numero
		elif char == '.':
			out_string += " " * indent * tab_size  + "putchar(*ptr);\n"
		elif char == ',':
			out_string += " " * indent * tab_size  + "*ptr=getchar();\n"
		elif char == '[':
			out_string += " " * indent * tab_size  + "while (*ptr) {\n"
			indent += 1
		elif char == ']':
			indent -= 1
			out_string += " " * indent * tab_size  + "}\n"
		digi = ""

print(header%out_string)