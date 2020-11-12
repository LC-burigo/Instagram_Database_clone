# Instagram_Database_clone
### In this repository, you can see an attempt to make a kind of instagram database with some operations!!!
The explanation of this project will be divide in 3 parts:
1. Tables databases flow chart
2. Functions
3. Packages and Programs

1) **Diagram**
<img src="Instagram_clone_diagram.png" width=400 border=blue>


2) **Functionalities**
  1. Insert a data or many datas in once to any table 
      >users \
      >photos \
      >likes \
      >comments \
      >follows \
      >tags \
      >photo_tags 
      
  2. Delete a data from any table
      >users \
      >photos \
      >likes \
      >comments \
      >follows \
      >tags \
      >photo_tags   
      
  3. Find the five oldest users registrated in the system
  
      Id| username | create_at|
      -----|-------|-----------|
      80|Darby_Herzog|2016-05-06 00:14:21|
      67|Emilio_Bernier52|2016-05-06 13:04:30|
      63|Elenor88|2016-05-08 01:30:41|
      95|Nicole71|2016-05-09 17:30:22|
      38|Jordyn.Jacobson2|2016-05-14 07:56:26|
      
  4. Find the most common day for people to register
      
      Day| Registrations |
      -----|-------|
      Sunday|17|
       
  5. Find the users who didn´t posted a single photo (inactive)
      
      username| 
      -----|
      Aniya_Hackett|
      Bartholome.Bernhard|
      Bethany20|
      Darby_Herzog|
      David.Osinski47|
      Duane60|
      Esmeralda.Mraz57|
      Esther.Zulauf61|
      Franco_Keebler64|
      Hulda.Macejkovic|
      Jaclyn81|
      Janelle.Nikolaus81|
      Jessyca_West|
      Julien_Schmidt|
      Kasandra_Homenick|
      Leslie67|
      Linnea59|
      Lucas_Burigo|
      Maxwell.Halvorson|
      Mckenna17|
      Mike.Auer39|
      Morgan.Kassulke|
      Nia_Haag|
      Ollie_Ledner37|
      Pearl7
      Rocio33|
      Samuel_Noll|
      Tierra.Trantow|
      
  6. Find the photos with more likes
      
      Image_url| photo_id | total_likes|
      -----|-------|-----------|
      https://jarret.name|145|48|
      
  7. Bring the count of Photos per users
      
      photo_per_user| 
      -----|
      2.5196|
      
  8. Select the most commom tags
  
      tag_name| total |
      -----|-------|
      smile|58|
      party|38|
      lol|24|
      fun|37|
      beach|42|
      
  9. Select the users which like more photos
  
      username| total_likes |
      --------|-------------|
      Aniya_Hackett|257|
      
      :pushpin:**OBS:** I add one more like from this user, to make her have 257 likes
      
  10. Select the users who comment the most
  
      username| total|
      --------|-------------|
      Aniya_Hackett|258|
      
      :pushpin:**OBS:** I add two more comments from this user, to make her have 258 comments
      
  11. Create a trigger that doesn´t allow the follower follow himself
  
      
3) **What you have to download**

MySQL Workbench | 
------------ |
[MySQL](https://dev.mysql.com/downloads/workbench/) | 
 
Pymysql | 
------------ |
[pip install PyMySQL](https://pypi.org/project/PyMySQL/) | 

:pushpin:**OBS:** I didn't do all the functions you can imagine, because that would be a lot. :sweat_smile:\
                  So, take a good look, understand how to make this connection python-Mysql, learn how todo somethings with the database, and be happy!:nerd_face:
