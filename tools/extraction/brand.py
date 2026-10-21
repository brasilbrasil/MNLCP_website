from PIL import Image, ImageOps
M='/hdd/projects/maui_nui_scp/MNLCP_website/_source_extracts/assets_work/pptx/ppt/media/'
B='/hdd/projects/maui_nui_scp/MNLCP_website/assets/img/brand/'
G=(108,177,70,255)   # #6CB146 footer band green
def op(fn): return Image.open(M+fn).convert('RGBA')
def crop(im,l,t,r,b):
    W,H=im.size; return im.crop((round(l*W),round(t*H),round(W*(1-r)),round(H*(1-b))))
def trim(im):
    return im.crop(im.getbbox())
def sh(im,h):
    return im.resize((round(im.width*h/im.height),h),Image.LANCZOS)
def save(im,name):
    im.save(B+name,optimize=True); print(name,im.size)
# seals
save(trim(op('image5.png')),'dlnr_seal.png')
save(trim(op('image6.png')),'dofaw_seal_nene.png')
# originals of fern art
save(op('image26.png'),'fern_art_footer_left_full.png')
save(op('image27.png'),'fern_art_footer_right_full.png')
save(op('image4.png'),'fern_art_band_left_full.png')
save(op('image2.png'),'fern_art_band_right_full.png')
save(op('image3.png'),'fern_art_frond_full.png')
L=crop(op('image26.png'),0,.61,.52,.05); R=crop(op('image27.png'),.6,.37,0,.37)
BL=crop(op('image4.png'),.05,.15,.01,.28); BR=crop(op('image2.png'),.06,.39,.02,0); BF=crop(op('image3.png'),0,0,0,.36)
save(L,'fern_footer_left_crop.png'); save(R,'fern_footer_right_crop.png')
# compact content-slide footer replica (native res, no upscale): 2400x158
h=min(L.height,R.height)
def band(w,h,left,right,bg=G):
    im=Image.new('RGBA',(w,h),bg)
    l=sh(left,h); r=sh(right,h)
    im.alpha_composite(l,(0,0)); im.alpha_composite(r,(w-r.width,0)); return im
save(band(2400,h,L,R),f'footer_band_compact_2400x{h}.png')
save(band(2400,h,L,R,(0,0,0,0)),f'footer_band_compact_2400x{h}_transparent.png')
# wide 2400x300 footer using larger band art (downscaled, crisp)
save(band(2400,300,BL,BR),'footer_band_2400x300.png')
save(band(2400,300,BL,BR,(0,0,0,0)),'footer_band_2400x300_transparent.png')
# tileable strip: mirrored right clump -> seamless both at centre and at edges
c=sh(BR,300); t=Image.new('RGBA',(c.width*2,300),G)
t.alpha_composite(c,(0,0)); t.alpha_composite(ImageOps.mirror(c),(c.width,0))
save(t,f'footer_fern_tile_{t.width}x300.png')
tt=Image.new('RGBA',(c.width*2,300),(0,0,0,0)); tt.alpha_composite(c,(0,0)); tt.alpha_composite(ImageOps.mirror(c),(c.width,0))
save(tt,f'footer_fern_tile_{t.width}x300_transparent.png')
# title-slide fern band (slides 1/16): band = bottom 30% of 16:9 slide
Wd=2400; Hs=round(Wd*10287000/18288000); Hb=round(Hs*0.30)
def titleband(bg):
    im=Image.new('RGBA',(Wd,Hb),bg)
    def place(art,x0,y0,w,h):
        a=art.resize((round(w*Wd),round(h*Hs)),Image.LANCZOS)
        im.alpha_composite(a,(round(x0*Wd),round((y0-0.70)*Hs)) if True else None)
    place(BL,0.0,0.70,0.388,0.30)
    place(BR,0.644,0.70,0.364,0.30)
    place(BF,0.700,0.848,0.188,0.152)
    return im
save(titleband((108,177,70,179)),f'fern_band_title_{Wd}x{Hb}_green70.png')
save(titleband((0,0,0,0)),f'fern_band_title_{Wd}x{Hb}_transparent.png')
# hero + band composite (no logos/text)
hero=Image.open(M+'image1.jpeg').convert('RGBA').resize((Wd,Hs),Image.LANCZOS)
hero.alpha_composite(titleband((108,177,70,179)),(0,Hs-Hb))
hero.convert('RGB').save(B+'hero_title_composite_2400.jpg',quality=82,optimize=True,progressive=True); print('hero_title_composite_2400.jpg',hero.size)
