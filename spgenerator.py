from PIL import Image, ImageDraw, ImageFont
import pandas as pd
df = pd.read_excel('data.xlsx');
df_s = pd.read_excel('style_settings.xlsx')
locations_df = pd.read_excel('poi_sp.xlsx')
locations = locations_df.set_index('Location').T.to_dict('list')
locations = {key: [int(coord.strip("[").strip("]").split(",")[0]), int(coord.strip("[").strip("]").split(",")[1])] for key, [coord] in locations.items()}
sp_poi_num = len(locations);
col2 = df_s.iloc[:,1]
col2 = col2[:7] 
data_1 = df.iloc[1:sp_poi_num+1, 1] ;team_1 = data_1.tolist();team_1 = [str(x) for x in team_1];
font_size = int(col2[0]);color_1 = eval(col2[1]);color_3 = eval(col2[3]);black = (0, 0, 0, 250);
image_path = 'sp.jpg' ;
font_path = col2[4];
image = Image.open(image_path)
draw = ImageDraw.Draw(image)
stroke_width = int(col2[5])
for i in range(sp_poi_num):
    if (team_1[i] != 'nan'):
        draw.text(
            (locations[list(locations.keys())[i]][0]- len(team_1[i])*font_size*0.125,locations[list(locations.keys())[i]][1]),  # 文字位置
            team_1[i],              # 文字内容
            font=ImageFont.truetype(font_path, size=font_size) ,         # 使用的字体
            fill=color_1,      # 文字颜色
            stroke_width=stroke_width,
            stroke_fill=black # 描边颜色
        )
draw.text(
            (100,100),  # 文字位置
            col2[6]+"(Storm Point)",              # 文字内容
            font=ImageFont.truetype(font_path, size = 0.8*font_size) ,         # 使用的字体，如果要使用中文的话，可以替换为相应的中文字体
            fill=color_3,      # 文字颜色
            stroke_width=stroke_width,
            stroke_fill=black  # 描边颜色
        ) 
image.save('Storm_Point.jpg') 
