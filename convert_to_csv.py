import pandas as pd
import os 

for folder_number in (range(1,100)):
    bb_info_path = "/home/prudhvi/Desktop/output/train/"+str(folder_number)+"/bb_info.txt"
    new_path = "/home/prudhvi/Desktop/output/train/"+str(folder_number)+"/bb_info_new.csv"

    df = pd.read_csv(new_path,sep=' ',header=0)
    # for index, row in df.iterrows():
    #     width = row['x2'],row['x1'],int(row['x2'])-int(row['x1']))

    # df['width'] = df.x2 - df.x1
    # df['height'] = df.y2 - df.y1
      
    #df['img'] = df.img + '.jpg'
    # for index, row in df.iterrows():
    #     df.loc[index,'img']=str(row[0])+'.jpg'
    #     # df.loc[index,'class']=str(folder_number)
    
   
    #     new_df = df.to_csv(new_path, ',',columns=['img','width','height','class','x1','y1','x2','y2'],index=False)



    filenames_list = []
    arr = os.listdir("/home/prudhvi/Desktop/output/train/"+str(folder_number))
    for i in range(0,len(arr)):
        filename = arr[i].split('.')[0]
        filenames_list.append(filename)

    # #print(filenames_list)
    
    #for folder_number in (range(1,100)):
    new_path = "/home/prudhvi/Desktop/output/train/"+str(folder_number)+"/bb_info_new.csv"

    df = pd.read_csv(new_path,sep=',',header=0)
    img_id = df['img']
    img_id_list = list(img_id)
    new_list = []
    for i in range(0,len(img_id_list)):
        new_list.append(str(img_id_list[i]))
    #print('New List',len(new_list))
    #print('Filenam List',len(filenames_list))


    new_list_final = []
    train_list_final =[]
    for element in filenames_list:
        #print(element)
         if element in new_list:
             new_list_final.append(element)
        #if element not in new_list:
         else:
            train_list_final.append(element)
    # print(train_list_final)
    
    # # c = open("/home/prudhvi/Desktop/output/test/"+str(folder_number)+"/bb_test.csv","w+")
    # # c.write("img,width,height,class,x1,y1,x2,y2\n")
    # # for i in range(0, len(train_list_final)):
    # #     for index, row in df.iterrows():
    # #         if(str(train_list_final[i])==str(row[0])):
    # #             c.write(str(row[0])+',' + str(row[1])+ ','+str(row[2])+','+str(row[3])+','+str(row[4])+','+str(row[5])+','+str(row[6])+','+str(row[7])+ '\n') 
    
    f = open("/home/prudhvi/Desktop/output/train/"+str(folder_number)+"/bb_new.csv","w+")
    f.write('img,width,height,class,x1,y1,x2,y2\n')        

    for i in range(0, len(new_list_final)):
        for index, row in df.iterrows():
            # print(new_list_final[i],row[0])
            if(str(new_list_final[i])==str(row[0])):
                #print(row)
              
                f.write(str(row[0])+',' + str(row[1])+ ','+str(row[2])+','+str(row[3])+','+str(row[4])+','+str(row[5])+','+str(row[6])+','+str(row[7])+ '\n')
                

                

                
    #             df.loc[index,'img']=str(row[0])+'.jpg'
    #             df.loc[index,'class']=str(folder_number)

    # print(new_list_final)