import pymupdf, json, re, sys, io
from PIL import Image
P=sys.argv[1]; OUT=sys.argv[2]; META=sys.argv[3]
doc=pymupdf.open(P)
def imgs(pn, ymin=0, ymax=800):
    rs=[pymupdf.Rect(i['bbox']) for i in doc[pn-1].get_image_info() if i['bbox'][1]>=ymin-1 and i['bbox'][3]<=ymax+1]
    u=rs[0]
    for r in rs[1:]: u|=r
    return u
# (id, slug, caption page, [ (page, rect or None->all images) ...], layout)
S=[
 ("1","teams_and_planning_processes",19,[(19,None)],None),
 ("2","combined_recovery_footprint",31,[(31,None)],None),
 ("3","persistence_by_taxonomic_group",34,[(34,None)],None),
 ("4","plant_recovery_footprint_panels",37,[(37,None)],None),
 ("5","kiwikiu_akohekohe_emergency_actions",43,[(43,None)],None),
 ("6","forest_bird_recovery_habitat",44,[(44,None)],None),
 ("7","seabird_recovery_footprint",48,[(48,None)],None),
 ("8","waterbird_recovery_habitat",54,[(53,None),(54,None)],"stack"),
 ("9","plant_recovery_and_priority_footprints",61,[(60,(126,73,486,285)),(60,(126,292,486,487)),(60,(126,495,486,693)),(61,None)],"grid"),
 ("10","plant_group_persistence",63,[(63,(117,324,478,624))],None),
 ("11","snail_exclosure_network",69,[(69,None)],None),
 ("12","terrestrial_arthropod_recovery_footprint",75,[(75,None)],None),
 ("13","terrestrial_arthropod_group_persistence",76,[(76,None)],None),
 ("14","multispecies_survey_areas",78,[(78,None)],None),
 ("15","aquatic_invertebrate_recovery_footprint",82,[(81,None),(82,None)],"stack"),
 ("16","aquatic_invertebrate_group_persistence",83,[(83,None)],None),
 ("17","maui_catchments_stream_flows",85,[(85,None)],None),
 ("18","hoary_bat_recovery_footprint",88,[(88,None)],None),
 ("19","combined_and_priority_footprints_panels",91,[(91,None)],None),
 ("20","target_richness_heat_map",92,[(92,None)],None),
 ("21","major_ecosystems",98,[(98,None)],None),
 ("22","remaining_habitat_quality",101,[(101,None)],None),
 ("23","management_potential",102,[(102,None)],None),
 ("24","plant_species_richness",104,[(104,None)],None),
 ("25","management_opportunities",105,[(105,None)],None),
 ("26","climate_vectors_and_habitat_quality",107,[(107,None)],None),
 ("27","ecosystem_opportunity_areas_1",108,[(108,None)],None),
 ("28","ecosystem_opportunity_areas_2",109,[(109,None)],None),
 ("29","monitoring_project_stages",121,[(120,None)],None),
 ("app2_1","four_islands_of_maui_nui",143,[(143,None)],None),
 ("app2_2","priority_threat_management_framework",145,[(144,None)],None),
 ("app2_3","persistence_elicitation_scalebar",147,[(146,None)],None),
 ("app2_4","persistence_estimates_17_species_groups",150,[(149,None)],None),
 ("app2_5","species_groups_secured_vs_cost",153,[(153,None)],None),
 ("app2_6","management_strategy_costs",154,[(154,None)],None),
 ("app2_s1","vertebrate_groups_secured_vs_cost",179,[(179,None)],None),
 ("app2_s2","invertebrate_groups_secured_vs_cost",180,[(180,None)],None),
 ("app2_s3","plant_groups_secured_vs_cost",182,[(182,None)],None),
]
def caption(pn, fid):
    t=re.sub(r'\s+',' ',doc[pn-1].get_text())
    num=fid.split('_')[-1].lstrip('s')
    m=re.search(r'(?:Figure|FIGURE)\s+'+num+r'[\.:]\s.*?(?:\.\s(?=[A-Z][a-z]+ [a-z])|$)',t)
    if not m: return None
    s=t[m.start():m.start()+700]
    return s
def render(pn, rect, dpi):
    pix=doc[pn-1].get_pixmap(clip=rect,dpi=dpi)
    return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
meta=[]
for fid,slug,cp,parts,layout in S:
    ims=[]
    for pn,r in parts:
        rect=pymupdf.Rect(r) if r else imgs(pn)
        rect=pymupdf.Rect(rect.x0-3,rect.y0-3,rect.x1+3,rect.y1+3)
        ims.append(render(pn,rect,220))
    if len(ims)==1: im=ims[0]
    elif layout=="stack":
        w=max(i.width for i in ims); h=sum(i.height for i in ims)+20*(len(ims)-1)
        im=Image.new("RGB",(w,h),"white"); y=0
        for i in ims: im.paste(i,((w-i.width)//2,y)); y+=i.height+20
    else:
        cw=max(i.width for i in ims); ch=max(i.height for i in ims)
        im=Image.new("RGB",(cw*2+20,ch*2+20),"white")
        for k,i in enumerate(ims): im.paste(i,((k%2)*(cw+20),(k//2)*(ch+20)))
    if im.width>1600: im=im.resize((1600,round(im.height*1600/im.width)),Image.LANCZOS)
    num=fid if fid.startswith('app') else f"{int(fid):02d}"
    fn=f"plan_fig_{num}_{slug}.png"
    im=im.quantize(colors=256,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE) if False else im
    im.save(f"{OUT}/{fn}",optimize=True)
    meta.append(dict(id=fid,file=fn,caption_page_pdf=cp,source_pages=[p for p,_ in parts],width=im.width,height=im.height,caption=caption(cp,fid)))
    print(fn,im.size)
json.dump(meta,open(META,'w'),indent=1,ensure_ascii=False)
