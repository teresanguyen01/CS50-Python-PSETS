from fpdf import FPDF

class PDF(): 
    def __init__(self, user_name): 
        self._pdf = FPDF(orientation='P', format='A4')
        self._pdf.add_page()

        self._pdf.set_font("Arial", size=24)
        self._pdf.cell(0, 10, "CS50 Shirtificate", ln=True, align='C')

        shirt_image = "shirtificate.png"
        image_width = 100
        self._pdf.image(shirt_image, x=(210 - image_width) / 2, y=self._pdf.get_y(), w=image_width)

        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font("Arial", size=16)
        self._pdf.set_y(self._pdf.get_y() + 50)
        self._pdf.cell(0, 10, user_name, ln=True, align='C')
        
    def save(self, user_name):
        self._pdf.output(user_name)


user_name = input("Username: ")
pdf = PDF(user_name)

pdf.save("shirtificate.pdf")
