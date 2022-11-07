#C:\\Users\\wonde\\Documents\\Anouk\\LPS\\Image\\jpg\\rmbg\\github\\LPS
import streamlit as st
import glob,os


def load_images():
   # image_files = glob.glob("./*/*.jpg")
    image_files = glob.glob("./resizes/*.jpg")
  #  st.write(image_files)
    name_files=[]

    for image_file in image_files:
        image_file = image_file.replace("\\","/")
        parts = image_file.split("_")
     
        if parts[-1] not in name_files:
            name_files.append(parts[-1])
            #names.append(parts[0])
    name_files.sort()
    #st.write(name_files)
        
    return image_files, name_files#, names

st.title("Mes Pets Shop")
st.write("""### Tableau de mes LPS """)
n = st.number_input("Sélectionne le nombre de colonne",1,5,4)
image_files, name_files = load_images()

#view_manuscripts = st.multiselect("select la collection", manuscripts)

view_images=[]
for image_file in image_files:
    #if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
        
groups=[]
#names_group=[]
for i in range(0,len(view_images),n):
    groups.append(view_images[i:i+n])

#for i in range(0,len(name_files),n): 
#   names_group.append(name_files[i:i+n])
                 
#st.write(groups) #pour controler la création de groupe

for group in groups:
    cols = st.columns(n)
    for i,image_file in enumerate(group):
        names_files = os.path.splitext(image_file)[0]
        names_files=names_files.split('\\')[-1]
        names_files=names_files.split('_')[-1]
        
        cols[i].image(image_file, caption=str(names_files))
#st.write(i,image_files[i])
