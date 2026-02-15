import pygame
import math
import sys

pygame.init()

# Konstanta
LEBAR=1000
TINGGI=700
FPS=60

# Warna Tema Ungu Gelap
UNGU_GELAP=(40,20,60)
UNGU_SEDANG=(80,50,120)
UNGU_TERANG=(130,90,180)
UNGU_NEON=(180,120,255)
PUTIH=(255,255,255)
ABU=(200,200,200)
ABU_GELAP=(100,100,100)
HIJAU=(100,255,100)
MERAH=(255,100,100)
KUNING=(255,255,100)

layar=pygame.display.set_mode((LEBAR,TINGGI))
pygame.display.set_caption("Kalkulator Advanced 2D")
clock=pygame.time.Clock()

font_besar=pygame.font.Font(None,42)
font_sedang=pygame.font.Font(None,32)
font_kecil=pygame.font.Font(None,24)

class Button:
    def __init__(self,x,y,w,h,text,color,hover_color):
        self.rect=pygame.Rect(x,y,w,h)
        self.text=text
        self.color=color
        self.hover_color=hover_color
        self.hovered=False
    def draw(self,surface):
        c=self.hover_color if self.hovered else self.color
        pygame.draw.rect(surface,c,self.rect,border_radius=10)
        pygame.draw.rect(surface,UNGU_NEON,self.rect,2,border_radius=10)
        txt=font_kecil.render(self.text,True,PUTIH)
        surface.blit(txt,(self.rect.centerx-txt.get_width()//2,self.rect.centery-txt.get_height()//2))
    def check_hover(self,pos):
        self.hovered=self.rect.collidepoint(pos)
    def clicked(self,pos,event):
        return event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and self.rect.collidepoint(pos)

class InputBox:
    def __init__(self,x,y,w,h,label=""):
        self.rect=pygame.Rect(x,y,w,h)
        self.text=""
        self.active=False
        self.label=label
    def handle_event(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            self.active=self.rect.collidepoint(event.pos)
        if event.type==pygame.KEYDOWN and self.active:
            if event.key==pygame.K_BACKSPACE:
                self.text=self.text[:-1]
            elif event.key==pygame.K_RETURN:
                return True
            elif len(self.text)<20:
                self.text+=event.unicode
        return False
    def draw(self,surface):
        color=UNGU_NEON if self.active else UNGU_TERANG
        pygame.draw.rect(surface,UNGU_SEDANG,self.rect,border_radius=5)
        pygame.draw.rect(surface,color,self.rect,2,border_radius=5)
        if self.label:
            lbl=font_kecil.render(self.label,True,ABU)
            surface.blit(lbl,(self.rect.x,self.rect.y-25))
        txt=font_kecil.render(self.text,True,PUTIH)
        surface.blit(txt,(self.rect.x+5,self.rect.centery-txt.get_height()//2))

def render_text(text,font,color,x,y,center=False):
    surf=font.render(text,True,color)
    if center:
        rect=surf.get_rect(center=(x,y))
    else:
        rect=surf.get_rect(topleft=(x,y))
    layar.blit(surf,rect)

def draw_header(title):
    pygame.draw.rect(layar,UNGU_SEDANG,(0,0,LEBAR,80))
    pygame.draw.rect(layar,UNGU_NEON,(0,78,LEBAR,2))
    render_text(title,font_besar,UNGU_NEON,LEBAR//2,40,center=True)

def menu_utama():
    buttons=[
        Button(50,100,220,80,"1. Operasi Dasar",UNGU_SEDANG,UNGU_TERANG),
        Button(290,100,220,80,"2. Pangkat & Akar",UNGU_SEDANG,UNGU_TERANG),
        Button(530,100,220,80,"3. Trigonometri",UNGU_SEDANG,UNGU_TERANG),
        Button(770,100,180,80,"4. Logaritma",UNGU_SEDANG,UNGU_TERANG),
        Button(50,200,220,80,"5. Faktorial",UNGU_SEDANG,UNGU_TERANG),
        Button(290,200,220,80,"6. Pers. Kuadrat",UNGU_SEDANG,UNGU_TERANG),
        Button(530,200,220,80,"7. Konversi Suhu",UNGU_SEDANG,UNGU_TERANG),
        Button(770,200,180,80,"8. Konv. Panjang",UNGU_SEDANG,UNGU_TERANG),
        Button(50,300,220,80,"9. Konv. Berat",UNGU_SEDANG,UNGU_TERANG),
        Button(290,300,220,80,"10. Sistem Bil.",UNGU_SEDANG,UNGU_TERANG),
        Button(530,300,220,80,"11. Statistik",UNGU_SEDANG,UNGU_TERANG),
        Button(770,300,180,80,"12. Matrix 2x2",UNGU_SEDANG,UNGU_TERANG),
        Button(LEBAR//2-100,600,200,60,"Keluar",MERAH,UNGU_TERANG)
    ]
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    if i<12: return str(i+1)
                    else: return "keluar"
        layar.fill(UNGU_GELAP)
        draw_header("KALKULATOR ADVANCED 2D")
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_operasi_dasar():
    inputs=[
        InputBox(LEBAR//2-150,150,300,40,"Angka 1:"),
        InputBox(LEBAR//2-150,220,300,40,"Angka 2:")
    ]
    buttons=[
        Button(100,300,120,50,"+",UNGU_SEDANG,UNGU_TERANG),
        Button(240,300,120,50,"-",UNGU_SEDANG,UNGU_TERANG),
        Button(380,300,120,50,"×",UNGU_SEDANG,UNGU_TERANG),
        Button(520,300,120,50,"÷",UNGU_SEDANG,UNGU_TERANG),
        Button(660,300,120,50,"%",UNGU_SEDANG,UNGU_TERANG),
        Button(800,300,120,50,"^",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            for inp in inputs:
                inp.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        a=float(inputs[0].text)
                        b=float(inputs[1].text)
                        if i==0: hasil=f"{a} + {b} = {a+b}"
                        elif i==1: hasil=f"{a} - {b} = {a-b}"
                        elif i==2: hasil=f"{a} × {b} = {a*b}"
                        elif i==3:
                            if b==0: hasil="ERROR: Tidak bisa bagi 0"
                            else: hasil=f"{a} ÷ {b} = {a/b}"
                        elif i==4: hasil=f"{a} % {b} = {a%b}"
                        elif i==5: hasil=f"{a} ^ {b} = {a**b}"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("OPERASI DASAR")
        for inp in inputs:
            inp.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,400,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,400,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,440,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_pangkat_akar():
    input1=InputBox(LEBAR//2-150,150,300,40,"Angka:")
    input2=InputBox(LEBAR//2-150,220,300,40,"Pangkat/Akar (n):")
    buttons=[
        Button(150,300,150,50,"x²",UNGU_SEDANG,UNGU_TERANG),
        Button(320,300,150,50,"x³",UNGU_SEDANG,UNGU_TERANG),
        Button(490,300,150,50,"√x",UNGU_SEDANG,UNGU_TERANG),
        Button(660,300,150,50,"ⁿ√x",UNGU_SEDANG,UNGU_TERANG),
        Button(380,370,150,50,"x^n",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            input2.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        x=float(input1.text)
                        if i==0: hasil=f"{x}² = {x**2}"
                        elif i==1: hasil=f"{x}³ = {x**3}"
                        elif i==2:
                            if x<0: hasil="ERROR: Tidak bisa akar negatif"
                            else: hasil=f"√{x} = {math.sqrt(x)}"
                        elif i==3:
                            n=int(input2.text)
                            if n==0: hasil="ERROR: Pangkat tidak boleh 0"
                            else: hasil=f"ⁿ√{x} (n={n}) = {x**(1/n)}"
                        elif i==4:
                            n=float(input2.text)
                            hasil=f"{x}^{n} = {x**n}"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("PANGKAT & AKAR")
        input1.draw(layar)
        input2.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,450,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,450,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,490,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_trigonometri():
    input1=InputBox(LEBAR//2-150,150,300,40,"Sudut (derajat):")
    buttons=[
        Button(150,220,120,50,"sin",UNGU_SEDANG,UNGU_TERANG),
        Button(290,220,120,50,"cos",UNGU_SEDANG,UNGU_TERANG),
        Button(430,220,120,50,"tan",UNGU_SEDANG,UNGU_TERANG),
        Button(570,220,120,50,"sec",UNGU_SEDANG,UNGU_TERANG),
        Button(710,220,120,50,"csc",UNGU_SEDANG,UNGU_TERANG),
        Button(380,290,120,50,"cot",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        deg=float(input1.text)
                        rad=math.radians(deg)
                        if i==0: hasil=f"sin({deg}°) = {math.sin(rad):.6f}"
                        elif i==1: hasil=f"cos({deg}°) = {math.cos(rad):.6f}"
                        elif i==2: hasil=f"tan({deg}°) = {math.tan(rad):.6f}"
                        elif i==3:
                            cos_val=math.cos(rad)
                            if abs(cos_val)<1e-10: hasil="ERROR: Sec undefined"
                            else: hasil=f"sec({deg}°) = {1/cos_val:.6f}"
                        elif i==4:
                            sin_val=math.sin(rad)
                            if abs(sin_val)<1e-10: hasil="ERROR: Csc undefined"
                            else: hasil=f"csc({deg}°) = {1/sin_val:.6f}"
                        elif i==5:
                            tan_val=math.tan(rad)
                            if abs(tan_val)<1e-10: hasil="ERROR: Cot undefined"
                            else: hasil=f"cot({deg}°) = {1/tan_val:.6f}"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("TRIGONOMETRI")
        input1.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,370,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,370,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,410,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_logaritma():
    input1=InputBox(LEBAR//2-150,150,300,40,"Angka:")
    input2=InputBox(LEBAR//2-150,220,300,40,"Base (untuk log_n):")
    buttons=[
        Button(300,300,120,50,"log₁₀",UNGU_SEDANG,UNGU_TERANG),
        Button(440,300,120,50,"ln",UNGU_SEDANG,UNGU_TERANG),
        Button(580,300,120,50,"log_n",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            input2.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        x=float(input1.text)
                        if x<=0: hasil="ERROR: Log hanya untuk x>0"; continue
                        if i==0: hasil=f"log₁₀({x}) = {math.log10(x):.6f}"
                        elif i==1: hasil=f"ln({x}) = {math.log(x):.6f}"
                        elif i==2:
                            base=float(input2.text)
                            if base<=0 or base==1: hasil="ERROR: Base harus >0 dan ≠1"
                            else: hasil=f"log_{base}({x}) = {math.log(x,base):.6f}"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("LOGARITMA")
        input1.draw(layar)
        input2.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,390,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,390,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,430,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_faktorial():
    input1=InputBox(LEBAR//2-150,150,300,40,"n:")
    input2=InputBox(LEBAR//2-150,220,300,40,"r (untuk P&C):")
    buttons=[
        Button(300,300,120,50,"n!",UNGU_SEDANG,UNGU_TERANG),
        Button(440,300,120,50,"nPr",UNGU_SEDANG,UNGU_TERANG),
        Button(580,300,120,50,"nCr",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            input2.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        n=int(input1.text)
                        if n<0: hasil="ERROR: n harus ≥ 0"; continue
                        if i==0: hasil=f"{n}! = {math.factorial(n)}"
                        else:
                            r=int(input2.text)
                            if r<0: hasil="ERROR: r harus ≥ 0"; continue
                            if r>n: hasil="ERROR: r tidak boleh > n"; continue
                            if i==1: hasil=f"P({n},{r}) = {math.perm(n,r)}"
                            elif i==2: hasil=f"C({n},{r}) = {math.comb(n,r)}"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("FAKTORIAL & KOMBINASI")
        input1.draw(layar)
        input2.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,390,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,390,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,430,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_persamaan_kuadrat():
    inputs=[
        InputBox(LEBAR//2-150,120,300,40,"a:"),
        InputBox(LEBAR//2-150,180,300,40,"b:"),
        InputBox(LEBAR//2-150,240,300,40,"c:")
    ]
    btn_hitung=Button(LEBAR//2-75,300,150,50,"Hitung",UNGU_SEDANG,UNGU_TERANG)
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=[]
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            for inp in inputs:
                inp.handle_event(event)
            if btn_hitung.clicked(pos,event):
                try:
                    a=float(inputs[0].text)
                    b=float(inputs[1].text)
                    c=float(inputs[2].text)
                    if a==0: hasil=["ERROR: Bukan pers. kuadrat (a=0)"]; continue
                    D=b**2-4*a*c
                    hasil=[f"Diskriminan D = {D:.2f}"]
                    if D>0:
                        x1=(-b+math.sqrt(D))/(2*a)
                        x2=(-b-math.sqrt(D))/(2*a)
                        hasil.append(f"x₁ = {x1:.4f}")
                        hasil.append(f"x₂ = {x2:.4f}")
                    elif D==0:
                        x=-b/(2*a)
                        hasil.append(f"x₁ = x₂ = {x:.4f}")
                    else:
                        real=-b/(2*a)
                        imag=math.sqrt(abs(D))/(2*a)
                        hasil.append(f"x₁ = {real:.4f} + {imag:.4f}i")
                        hasil.append(f"x₂ = {real:.4f} - {imag:.4f}i")
                except: hasil=["ERROR: Input tidak valid"]
        layar.fill(UNGU_GELAP)
        draw_header("PERSAMAAN KUADRAT (ax²+bx+c=0)")
        for inp in inputs:
            inp.draw(layar)
        btn_hitung.check_hover(pos)
        btn_hitung.draw(layar)
        if hasil:
            y_start=380
            for i,h in enumerate(hasil):
                color=HIJAU if "ERROR" not in h else MERAH
                render_text(h,font_kecil,color,LEBAR//2,y_start+i*30,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_konversi_suhu():
    input1=InputBox(LEBAR//2-150,150,300,40,"Nilai:")
    buttons=[
        Button(100,230,150,50,"C→F",UNGU_SEDANG,UNGU_TERANG),
        Button(270,230,150,50,"C→K",UNGU_SEDANG,UNGU_TERANG),
        Button(440,230,150,50,"C→R",UNGU_SEDANG,UNGU_TERANG),
        Button(610,230,150,50,"F→C",UNGU_SEDANG,UNGU_TERANG),
        Button(780,230,150,50,"K→C",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        val=float(input1.text)
                        if i==0: hasil=f"{val}°C = {(val*9/5)+32:.2f}°F"
                        elif i==1: hasil=f"{val}°C = {val+273.15:.2f}K"
                        elif i==2: hasil=f"{val}°C = {val*4/5:.2f}°R"
                        elif i==3: hasil=f"{val}°F = {(val-32)*5/9:.2f}°C"
                        elif i==4: hasil=f"{val}K = {val-273.15:.2f}°C"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("KONVERSI SUHU")
        input1.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,320,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,320,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,360,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_konversi_panjang():
    input1=InputBox(LEBAR//2-150,150,300,40,"Nilai:")
    buttons=[
        Button(80,230,140,50,"m→km",UNGU_SEDANG,UNGU_TERANG),
        Button(240,230,140,50,"m→cm",UNGU_SEDANG,UNGU_TERANG),
        Button(400,230,140,50,"m→mm",UNGU_SEDANG,UNGU_TERANG),
        Button(560,230,140,50,"m→ft",UNGU_SEDANG,UNGU_TERANG),
        Button(720,230,140,50,"km→mil",UNGU_SEDANG,UNGU_TERANG),
        Button(320,300,140,50,"mil→km",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        val=float(input1.text)
                        if i==0: hasil=f"{val}m = {val/1000:.4f}km"
                        elif i==1: hasil=f"{val}m = {val*100:.2f}cm"
                        elif i==2: hasil=f"{val}m = {val*1000:.2f}mm"
                        elif i==3: hasil=f"{val}m = {val*3.28084:.4f}ft"
                        elif i==4: hasil=f"{val}km = {val*0.621371:.4f}mil"
                        elif i==5: hasil=f"{val}mil = {val*1.60934:.4f}km"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("KONVERSI PANJANG")
        input1.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,380,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,380,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,420,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_konversi_berat():
    input1=InputBox(LEBAR//2-150,150,300,40,"Nilai:")
    buttons=[
        Button(160,230,140,50,"kg→g",UNGU_SEDANG,UNGU_TERANG),
        Button(320,230,140,50,"kg→lb",UNGU_SEDANG,UNGU_TERANG),
        Button(480,230,140,50,"kg→ton",UNGU_SEDANG,UNGU_TERANG),
        Button(640,230,140,50,"kg→ons",UNGU_SEDANG,UNGU_TERANG),
        Button(360,300,140,50,"lb→kg",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        val=float(input1.text)
                        if i==0: hasil=f"{val}kg = {val*1000:.2f}g"
                        elif i==1: hasil=f"{val}kg = {val*2.20462:.4f}lb"
                        elif i==2: hasil=f"{val}kg = {val/1000:.6f}ton"
                        elif i==3: hasil=f"{val}kg = {val*10:.2f}ons"
                        elif i==4: hasil=f"{val}lb = {val/2.20462:.4f}kg"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("KONVERSI BERAT")
        input1.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,380,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,380,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,420,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_statistik():
    input1=InputBox(50,120,LEBAR-100,40,"Data (pisahkan dengan spasi):")
    btn_hitung=Button(LEBAR//2-75,180,150,50,"Hitung",UNGU_SEDANG,UNGU_TERANG)
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=[]
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            if btn_hitung.clicked(pos,event):
                try:
                    data=list(map(float,input1.text.split()))
                    if len(data)==0: hasil=["ERROR: Data kosong"]; continue
                    n=len(data)
                    mean=sum(data)/n
                    data_sorted=sorted(data)
                    if n%2==0: median=(data_sorted[n//2-1]+data_sorted[n//2])/2
                    else: median=data_sorted[n//2]
                    variance=sum((x-mean)**2 for x in data)/n
                    std_dev=math.sqrt(variance)
                    hasil=[
                        f"N: {n} | Mean: {mean:.4f}",
                        f"Median: {median:.4f} | Min: {min(data):.2f}",
                        f"Max: {max(data):.2f} | Std Dev: {std_dev:.4f}"
                    ]
                except: hasil=["ERROR: Input tidak valid"]
        layar.fill(UNGU_GELAP)
        draw_header("STATISTIK")
        input1.draw(layar)
        btn_hitung.check_hover(pos)
        btn_hitung.draw(layar)
        if hasil:
            y_start=270
            for i,h in enumerate(hasil):
                color=HIJAU if "ERROR" not in h else MERAH
                render_text(h,font_sedang,color,LEBAR//2,y_start+i*40,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_matrix():
    inputs_a=[
        InputBox(100,120,100,35,"a11:"),
        InputBox(220,120,100,35,"a12:"),
        InputBox(100,170,100,35,"a21:"),
        InputBox(220,170,100,35,"a22:")
    ]
    inputs_b=[
        InputBox(480,120,100,35,"b11:"),
        InputBox(600,120,100,35,"b12:"),
        InputBox(480,170,100,35,"b21:"),
        InputBox(600,170,100,35,"b22:")
    ]
    buttons=[
        Button(250,240,120,50,"A+B",UNGU_SEDANG,UNGU_TERANG),
        Button(390,240,120,50,"A×B",UNGU_SEDANG,UNGU_TERANG),
        Button(530,240,120,50,"Det(A)",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=[]
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            for inp in inputs_a+inputs_b:
                inp.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        a11=float(inputs_a[0].text)
                        a12=float(inputs_a[1].text)
                        a21=float(inputs_a[2].text)
                        a22=float(inputs_a[3].text)
                        if i==0:
                            b11=float(inputs_b[0].text)
                            b12=float(inputs_b[1].text)
                            b21=float(inputs_b[2].text)
                            b22=float(inputs_b[3].text)
                            hasil=[
                                "Hasil A + B:",
                                f"[{a11+b11:.2f}  {a12+b12:.2f}]",
                                f"[{a21+b21:.2f}  {a22+b22:.2f}]"
                            ]
                        elif i==1:
                            b11=float(inputs_b[0].text)
                            b12=float(inputs_b[1].text)
                            b21=float(inputs_b[2].text)
                            b22=float(inputs_b[3].text)
                            c11=a11*b11+a12*b21
                            c12=a11*b12+a12*b22
                            c21=a21*b11+a22*b21
                            c22=a21*b12+a22*b22
                            hasil=[
                                "Hasil A × B:",
                                f"[{c11:.2f}  {c12:.2f}]",
                                f"[{c21:.2f}  {c22:.2f}]"
                            ]
                        elif i==2:
                            det=a11*a22-a12*a21
                            hasil=[f"Determinan A = {det:.4f}"]
                    except: hasil=["ERROR: Input tidak valid"]
        layar.fill(UNGU_GELAP)
        draw_header("MATRIX 2x2")
        render_text("Matrix A:",font_kecil,UNGU_NEON,50,95)
        render_text("Matrix B:",font_kecil,UNGU_NEON,430,95)
        for inp in inputs_a+inputs_b:
            inp.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            y_start=320
            for i,h in enumerate(hasil):
                color=HIJAU if "ERROR" not in h else MERAH
                render_text(h,font_sedang,color,LEBAR//2,y_start+i*35,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def scene_sistem_bilangan():
    input1=InputBox(LEBAR//2-150,150,300,40,"Nilai:")
    buttons=[
        Button(120,230,160,50,"Dec→Bin",UNGU_SEDANG,UNGU_TERANG),
        Button(300,230,160,50,"Dec→Oct",UNGU_SEDANG,UNGU_TERANG),
        Button(480,230,160,50,"Dec→Hex",UNGU_SEDANG,UNGU_TERANG),
        Button(660,230,160,50,"Bin→Dec",UNGU_SEDANG,UNGU_TERANG),
        Button(240,300,160,50,"Oct→Dec",UNGU_SEDANG,UNGU_TERANG),
        Button(420,300,160,50,"Hex→Dec",UNGU_SEDANG,UNGU_TERANG)
    ]
    btn_back=Button(50,600,150,50,"Kembali",MERAH,UNGU_TERANG)
    hasil=""
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "keluar"
            if btn_back.clicked(pos,event):
                return "menu"
            input1.handle_event(event)
            for i,btn in enumerate(buttons):
                if btn.clicked(pos,event):
                    try:
                        if i==0:
                            val=int(input1.text)
                            hasil=f"{val}₁₀ = {bin(val)[2:]}₂"
                        elif i==1:
                            val=int(input1.text)
                            hasil=f"{val}₁₀ = {oct(val)[2:]}₈"
                        elif i==2:
                            val=int(input1.text)
                            hasil=f"{val}₁₀ = {hex(val)[2:].upper()}₁₆"
                        elif i==3:
                            val=input1.text
                            hasil=f"{val}₂ = {int(val,2)}₁₀"
                        elif i==4:
                            val=input1.text
                            hasil=f"{val}₈ = {int(val,8)}₁₀"
                        elif i==5:
                            val=input1.text
                            hasil=f"{val}₁₆ = {int(val,16)}₁₀"
                    except: hasil="ERROR: Input tidak valid"
        layar.fill(UNGU_GELAP)
        draw_header("SISTEM BILANGAN")
        input1.draw(layar)
        for btn in buttons:
            btn.check_hover(pos)
            btn.draw(layar)
        if hasil:
            pygame.draw.rect(layar,UNGU_SEDANG,(50,380,LEBAR-100,80),border_radius=10)
            pygame.draw.rect(layar,UNGU_NEON,(50,380,LEBAR-100,80),2,border_radius=10)
            color=HIJAU if "ERROR" not in hasil else MERAH
            render_text(hasil,font_sedang,color,LEBAR//2,420,center=True)
        btn_back.check_hover(pos)
        btn_back.draw(layar)
        pygame.display.flip()
        clock.tick(FPS)

def main():
    scene="menu"
    while True:
        if scene=="menu": scene=menu_utama()
        elif scene=="1": scene=scene_operasi_dasar()
        elif scene=="2": scene=scene_pangkat_akar()
        elif scene=="3": scene=scene_trigonometri()
        elif scene=="4": scene=scene_logaritma()
        elif scene=="5": scene=scene_faktorial()
        elif scene=="6": scene=scene_persamaan_kuadrat()
        elif scene=="7": scene=scene_konversi_suhu()
        elif scene=="8": scene=scene_konversi_panjang()
        elif scene=="9": scene=scene_konversi_berat()
        elif scene=="10": scene=scene_sistem_bilangan()
        elif scene=="11": scene=scene_statistik()
        elif scene=="12": scene=scene_matrix()
        elif scene=="keluar": break
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()