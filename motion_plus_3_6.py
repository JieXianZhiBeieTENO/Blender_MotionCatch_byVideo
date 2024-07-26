bl_info = {
    "name" : "动捕",
    "author" : "尐贤之辈のTENO",
    "description" : "顾名思义(当然，这个插件是以Minecraft人物为模板)",
    "blender" : (3, 3, 0),
    "version" : (1, 0, 0),
    "location" : "View 3D > Motioncatch",
    "warning" : "这是本人第二次制作插件，如有问题也请多多包涵╭(╰▽╯)╮",
    "category" : "Animation",
    "doc_url": "",
    "tracker_url": "https://space.bilibili.com/1729654169"
}

    
import sys,time,bpy,os,math
from bl_operators.presets import AddPresetBase
from bpy.props import (
        IntProperty,
        BoolProperty,
        StringProperty,
        PointerProperty,
        FloatVectorProperty,
        IntVectorProperty
    )
try:
    import cv2
    import mediapipe as m
    bpy.types.Scene.Motion_catch_isInstall=1
except:
    bpy.types.Scene.Motion_catch_isInstall=0
Path=bpy.utils.resource_path('USER') + '\\scripts\\presets\\kumopult_bac\\MC_STEVE_BONES_MAPPING_MOTIONBODYCATCH.py'
if not os.access(Path,os.F_OK):
    bpy.types.Scene.Motion_catch_isInstall=0

class Install(bpy.types.Operator):
    bl_label="安装前置"
    bl_idname="motioncatch.install"
    bl_description = "安装mediapipe、cv2与一个Bone Animation Copy Tool的预设"
    def execute(self,context):
        import subprocess
        path1=bpy.utils.resource_path('USER') + '\\scripts\\presets\\kumopult_bac'
        Path=path1+'\\MC_STEVE_BONES_MAPPING_MOTIONBODYCATCH.py'
        bpy.ops.wm.console_toggle()
        python_exe=os.path.join(sys.prefix,'bin','python.exe')
        subprocess.call([python_exe,'-m','ensurepip'])
        subprocess.call([python_exe,'-m','pip','install','mediapipe','-i','https://pypi.mirrors.ustc.edu.cn/simple/'])
        subprocess.call([python_exe,'-m','pip','install','cv2','-i','https://pypi.mirrors.ustc.edu.cn/simple/'])
        #subprocess.call([python_exe,'-m','pip','install','sympy','-i','https://pypi.mirrors.ustc.edu.cn/simple/'])
        if not os.path.exists(path1):
            os.makedirs(path1)
        with open(Path,'w') as f:
            f.write('''import bpy
s = bpy.context.scene.kumopult_bac_owner.data.kumopult_bac

s.mappings.clear()
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Body'
item_sub_1.owner = 'Body'
item_sub_1.target = 'body_bot'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.11047934740781784, -3.1415927410125732, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Chest'
item_sub_1.owner = 'Chest'
item_sub_1.target = 'body_mid'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.1843067854642868, -3.1415927410125732, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Head'
item_sub_1.owner = 'Head'
item_sub_1.target = 'head'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (-0.229859858751297, 3.1415927410125732, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Arm:Left:Upper'
item_sub_1.owner = 'Arm:Left:Upper'
item_sub_1.target = 'L_arm_top'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.0, 0.0, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Arm:Left:Lower'
item_sub_1.owner = 'Arm:Left:Lower'
item_sub_1.target = 'L_arm_bot'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.0, 1.0063568353652954, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Arm:Right:Upper'
item_sub_1.owner = 'Arm:Right:Upper'
item_sub_1.target = 'R_arm_top'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.0, 0.0, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Arm:Right:Lower'
item_sub_1.owner = 'Arm:Right:Lower'
item_sub_1.target = 'R_arm_bot'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.0, -1.0168288946151733, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Leg:Right:Upper'
item_sub_1.owner = 'Leg:Right:Upper'
item_sub_1.target = 'R_leg_top'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.1759292036294937, 3.1415927410125732, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Leg:Right:Lower'
item_sub_1.owner = 'Leg:Right:Lower'
item_sub_1.target = 'R_leg_bot'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.0, 3.008075475692749, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Leg:Left:Upper'
item_sub_1.owner = 'Leg:Left:Upper'
item_sub_1.target = 'L_leg_top'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.06702064722776413, 3.1415927410125732, 0.0)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
item_sub_1 = s.mappings.add()
item_sub_1.name = ''
item_sub_1.selected_owner = 'Leg:Left:Lower'
item_sub_1.owner = 'Leg:Left:Lower'
item_sub_1.target = 'L_leg_bot'
item_sub_1.has_rotoffs = True
item_sub_1.has_loccopy = False
item_sub_1.has_ik = False
item_sub_1.offset = (0.0, -3.0023157596588135, 0.06021386384963989)
item_sub_1.loc_axis = (True, True, True)
item_sub_1.ik_influence = 1.0
item_sub_1.selected = False
s.selected_count = 0
            ''')
        if not bpy.types.Scene.Motion_catch_isInstall:
            cls=(Motion_catch,
            fd_pe_add,
            fd_pe_rem,
            MOTIONCATCH_MT_face_presets_menu,
            Add_Preset,
            MOTIONCATCH_PT_ui_panel,
            Add_Bones_Preset,
            Rem_Bones_Preset,
            MOTIONCATCH_MT_Face_Bones_Presets_menu,
            MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset,
            real_MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset,
            MOTIONCATCH_MT_is_Face_Bones_Presets_Reset_menu,
            face_bake,
            ex_pr_add,
            ex_pr_apply,
            ex_pr_rem,
            MOTIONCATCH_MT_extra_Face_Bones_Presets_menu,
            Add_extra_Bones_Preset,
            MOTIONCATCH_MT_error_menu)
            for Class in cls:
                bpy.utils.register_class(Class)
            bpy.types.Scene.Motion_catch_isInstall=1
        bpy.ops.wm.console_toggle()
        return {"FINISHED"}
    
class ins_in_pref(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout=self.layout
        row = layout.row()
        if bpy.types.Scene.Motion_catch_isInstall:
            row.operator(Install.bl_idname, icon="CONSOLE",text="重新安装前置")
        else:
            row.operator(Install.bl_idname, icon="CONSOLE",text="安装前置")
        
def FABO():
    return ['le_br','ri_br','le_eye','ri_eye','le_mouse','ri_mouse','top_mouse','bot_mouse','le_eyeb','ri_eyeb']
def FAEM():
    return ['le_br_le','le_br_ri','ri_br_le','ri_br_ri','le_eye','ri_eye','top_mo','bot_mo','le_mo','ri_mo','le_eyeb','ri_eyeb']
def motion_catch():
    global T1,T2,times,Count,re_bodyNose
    su,img = source.read()
    if not su:
        return 1
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    bpy.context.scene.frame_current=bpy.context.scene.frame_start+int(bpy.context.scene.render.fps/int(per_fps)*Count)
    if bpy.context.scene.frame_current>=bpy.context.scene.frame_end and tools.Is_align_framend:
        bpy.context.scene.frame_end=bpy.context.scene.frame_current
    if tools.Is_body:
        results = pose.process(imgRGB)
        if results.pose_landmarks:
            Mdraw.draw_landmarks(img,results.pose_landmarks,Mpose.POSE_CONNECTIONS)
                
            varss=['head_top','body_top_h_b','body_bot','L_arm_top','L_arm_mid','L_arm_bot','R_arm_top','R_arm_mid','R_arm_bot','L_leg_top','L_leg_mid','L_leg_bot','R_leg_top','R_leg_mid','R_leg_bot','nose']
            vars=['L_arm_top','L_arm_mid','L_arm_bot','R_arm_top','R_arm_mid','R_arm_bot','L_leg_top','L_leg_mid','L_leg_bot','R_leg_top','R_leg_mid','R_leg_bot','nose']
            if 1:
                if times:
                    for i in varss:
                        exec(f"global re_{i};re_{i}=[0,0,0]")
                moca=results.pose_landmarks.landmark
                head_top=avg(moca[7],moca[8],re_head_top)
                body_top_h_b=avg(moca[11],moca[12],re_body_top_h_b)
                body_bot=avg(moca[23],moca[24],re_body_bot)
                cache_l=[12,14,16,11,13,15,24,26,28,23,25,27,0]
                for i in range(len(vars)):
                    cachE1=vars[i]
                    cachE2=cache_l[i]
                    exec(f"global {cachE1};{cachE1}=nor(moca[{cachE2}],re_{cachE1})")
                for i in varss:
                    exec(f"global re_{i};re_{i}=bpy.data.objects['{i}'].matrix_world.translation")
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.data.objects[i].select_set(True)
                    exec(f'bpy.ops.transform.translate(value={i})')
                    bpy.ops.anim.keyframe_insert_by_name(type="Location")
                    
    if tools.Is_hands_catch and tools.Is_body:
        EM_1=['1_1', '1_2', '1_3', '1_4', '2_1', '2_2', '2_3', '2_4', '3_1', '3_2', '3_3', '3_4', '4_1', '4_2', '4_3', '4_4', '5_1', '5_2', '5_3', '5_4']
        EM_2=['6_1', '6_2', '6_3', '6_4', '7_1', '7_2', '7_3', '7_4', '8_1', '8_2', '8_3', '8_4', '9_1', '9_2', '9_3', '9_4', '10_1', '10_2', '10_3', '10_4']
        
        results2=mh.process(imgRGB)
        
        if results2.multi_hand_landmarks:
            for c,t in enumerate(results2.multi_hand_landmarks):
                Mdraw.draw_landmarks(img,results2.multi_hand_landmarks[c],mH.HAND_CONNECTIONS)
                if c==3:
                    break
                if 1:
                    if c:
                        EM=EM_2
                    else:
                        EM=EM_1
                    if times:
                        for i in EM_1+EM_2:
                            exec(f"global re_{i};re_{i}=[0,0,0]")
                    moca1=results2.multi_hand_landmarks[c].landmark
                    cache_h=[q for q in range(1,21)]
                    for c1,i in enumerate(EM):
                        cachE2=cache_h[c1]
                        exec(f"global _{i};_{i}=nor(moca1[{cachE2}],re_{i})")
                        exec(f"global re_{i};re_{i}=bpy.data.objects['{i}'].matrix_world.translation")
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.data.objects[i].select_set(True)
                        exec(f'bpy.ops.transform.translate(value=_{i})')
                        bpy.ops.anim.keyframe_insert_by_name(type="Location")
            
          
    if tools.Is_Face:
        EM=FAEM()
        po_id=[63,66,296,293,159,386,13,14,61,291,468,473]
        results1=mf.process(imgRGB)
        if results1.multi_face_landmarks:
            if tools.Is_ShowFace:
                Mdraw.draw_landmarks(img,results1.multi_face_landmarks[0],mF.FACEMESH_TESSELATION)
            if tools.Is_ShowFaceEdge:
                Mdraw.draw_landmarks(img,results1.multi_face_landmarks[0],mF.FACEMESH_CONTOURS)
            faca=results1.multi_face_landmarks[0].landmark
            if 1:
                if times:
                    for i in EM:
                        exec(f"global re_{i};re_{i}=0")
                        if i in ['le_br_le','le_br_ri','ri_br_le','ri_br_ri','le_mo','ri_mo','le_eyeb','ri_eyeb']:
                            exec(f"global re_{i}_x;re_{i}_x=0")
                for i in range(len(EM)):
                    bpy.ops.object.select_all(action='DESELECT')
                    emm=EM[i]
                    bpy.data.objects[emm].select_set(True)
                    if not 8<=i<=9:
                        if i!=1 and i!=3:
                            e=0
                        else:
                            e=1
                        exec(f'g=faca[po_id[{i}]].y-bpy.context.scene.Motion_catch_fa_defa[po_id[{i}-e]][1];g=g-re_{emm};bpy.ops.transform.translate(value=(0,0,g))')
                        exec(f"global re_{emm};re_{emm}=bpy.data.objects['{emm}'].matrix_world.translation[2]")
                    if i<=3 or 8<=i<=11:
                        exec(f'g=faca[po_id[{i}]].x-bpy.context.scene.Motion_catch_fa_defa[po_id[{i}-e]][0];g=g-re_{emm}_x;bpy.ops.transform.translate(value=(g,0,0))')
                        exec(f"global re_{emm}_x;re_{emm}_x=bpy.data.objects['{emm}'].matrix_world.translation[0]")
                    bpy.ops.anim.keyframe_insert_by_name(type="Location")
            if tools.Is_ShowFaceline:
                h,w=img.shape[0],img.shape[1]
                Lines=[[0,1],[2,3],[6,8],[7,9],[6,9],[7,8]]
                for i in Lines:
                    exec('cv2.line(img,(int(faca[po_id[i[0]]].x*w),int(faca[po_id[i[0]]].y*h)),(int(faca[po_id[i[1]]].x*w),int(faca[po_id[i[1]]].y*h)),(0,255,100),3)')
                for i in [4,5,10,11]:
                    exec('cv2.circle(img,(int(faca[po_id[i]].x*w),int(faca[po_id[i]].y*h)),3,(0,255,0),-1)')
                
    times=0
    Count+=1
    T1 = time.time()
    FPS = int(1/(T1-T2))
    T2 = T1
    imy,imx,imdepth=img.shape
    if imy>1050:
        size_level=math.ceil(imy/1050)
        img=cv2.resize(img,(int(imx/size_level),int(imy/size_level)))
    elif imx>1050:
        size_level=math.ceil(imx/1050)
        img=cv2.resize(img,(int(imx/size_level),int(imy/size_level)))
    if FPS>=12:
        FPS_Co=(255,255,255)
    else:
        FPS_Co=(0,0,255)
    cv2.putText(img,"FPS:"+str(FPS),(10,50),cv2.FONT_HERSHEY_DUPLEX,1,FPS_Co,2)
    cv2.putText(img,"Click leftmouse on",(10,70),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1)
    cv2.putText(img,"any interface of blender to quit",(10,87),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1)
    #print(imy,imx,imdepth,img.shape)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    return 0

def face_spawn_cache():
    EM=FAEM()
    Bo=FABO()
    Fo_group=['le_br_le','ri_br_le','le_eye','ri_eye','le_mo','ri_mo','top_mo','bot_mo','le_eyeb','ri_eyeb']
    Tr_group=['le_br_ri','ri_br_ri']
    try:
        bpy.ops.object.mode_set(mode='OBJECT')
    except:
        pass
    for i in EM:
        bpy.ops.object.empty_add(type='PLAIN_AXES', radius=0.05, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.selected_objects[0].name=i
    
    bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.context.selected_objects[0].name="fAcEcaTcH"
    bpy.context.selected_objects[0].data.name="fAcEcaTcH"
    bpy.context.selected_objects[0]["Is_Facecatch(Don't touch it!)"]=True
    bpy.ops.armature.select_all(action='SELECT')
    for i in range(len(Bo)):
        bpy.context.selected_bones[0].name=Bo[i]
        bpy.ops.object.mode_set(mode='POSE')
        if i==0:
            bpy.data.objects["fAcEcaTcH"].pose.bones[Bo[i]].constraints.new("COPY_LOCATION").target=bpy.data.objects[Fo_group[i]]
            bpy.data.objects["fAcEcaTcH"].pose.bones[Bo[i]].constraints.new("DAMPED_TRACK").target=bpy.data.objects[Tr_group[i]]
        else:
            bpy.data.objects["fAcEcaTcH"].pose.bones[Bo[i]].constraints[0].target=bpy.data.objects[Fo_group[i]]
        if i==1:
            bpy.data.objects["fAcEcaTcH"].pose.bones[Bo[i]].constraints[1].target=bpy.data.objects[Tr_group[i]]
        if i==2:
            bpy.data.objects["fAcEcaTcH"].pose.bones[Bo[i]].constraints.remove(bpy.data.objects["fAcEcaTcH"].pose.bones[Bo[i]].constraints[1])
        bpy.ops.object.mode_set(mode='EDIT')
        if i!=9:
            bpy.ops.armature.duplicate_move()
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.empty_add(type='SPHERE', radius=0.65, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.context.selected_objects[0].name="面捕空物体父级"
    bpy.context.selected_objects[0].name="面捕空物体父级"
    bpy.data.objects["面捕空物体父级"]['mu']=[1.0,1,1]
    bpy.data.objects["面捕空物体父级"]['add']=[0.0,0.0,0.0]
    for i in EM:
        bpy.data.objects[i].parent=bpy.data.objects["面捕空物体父级"]
    bpy.ops.object.empty_add(type='SPHERE', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.context.selected_objects[0].name="面部父级"
    bpy.context.selected_objects[0].name="面部父级"
    bpy.data.objects["面捕空物体父级"].parent=bpy.data.objects["面部父级"]
    bpy.data.objects["fAcEcaTcH"].parent=bpy.data.objects["面部父级"]
    for i in EM+["面捕空物体父级","面部父级","fAcEcaTcH"]:
        bpy.data.objects[i].select_set(True)
    bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name="Face_Track_Empty_And_Bones")
    '''for i in Bo:
        if i in ['le_mouse','ri_mouse']:
            bpy.data.objects["fAcEcaTcH"].pose.bones[i]["view_X_bone"]=[0,1.0,0]
        else:
            bpy.data.objects["fAcEcaTcH"].pose.bones[i]["view_X_bone"]=[0,0,-1.0]
        for o in range(3):
            sc_dr=bpy.data.objects["fAcEcaTcH"].pose.bones[i].driver_add("location")[o]
            sc_dr.driver.use_self=True
            sc_dr.driver.expression=f"self.location[2]*self['view_X_bone'][{o}]"'''
        
def body_spawn_cache():
    Co=0
    Mo_ca = bpy.context.scene.Motion_catch
    Fo_group=['body_bot','body_top_h_b','L_arm_top','L_arm_mid','R_arm_top','R_arm_mid','L_leg_top','L_leg_mid','R_leg_top','R_leg_mid']
    Tr_group=['body_top_h_b','head_top','L_arm_mid','L_arm_bot','R_arm_mid','R_arm_bot','L_leg_mid','L_leg_bot','R_leg_mid','R_leg_bot']
    EM=['body_bot','body_top_h_b','head_top','L_arm_top','L_arm_mid','L_arm_bot','R_arm_top','R_arm_mid','R_arm_bot','L_leg_top','L_leg_mid','L_leg_bot','R_leg_top','R_leg_mid','R_leg_bot',"nose"]
    
    try:
        bpy.ops.object.mode_set(mode='OBJECT')
    except:
        pass
    
    if Mo_ca.Is_hands_catch:
        EM_hands=['1_1', '1_2', '1_3', '1_4', '2_1', '2_2', '2_3', '2_4', '3_1', '3_2', '3_3', '3_4', '4_1', '4_2', '4_3', '4_4', '5_1', '5_2', '5_3', '5_4', '6_1', '6_2', '6_3', '6_4', '7_1', '7_2', '7_3', '7_4', '8_1', '8_2', '8_3', '8_4', '9_1', '9_2', '9_3', '9_4', '10_1', '10_2', '10_3', '10_4']
        Tr_hands=['1_2', '1_3', '1_4', '2_2', '2_3', '2_4', '3_2', '3_3', '3_4', '4_2', '4_3', '4_4', '5_2', '5_3', '5_4', '6_2', '6_3', '6_4', '7_2', '7_3', '7_4', '8_2', '8_3', '8_4', '9_2', '9_3', '9_4', '10_2', '10_3', '10_4']
        Fo_hands=['1_1', '1_2', '1_3', '2_1', '2_2', '2_3', '3_1', '3_2', '3_3', '4_1', '4_2', '4_3', '5_1', '5_2', '5_3', '6_1', '6_2', '6_3', '7_1', '7_2', '7_3', '8_1', '8_2', '8_3', '9_1', '9_2', '9_3', '10_1', '10_2', '10_3']
    else:
        EM_hands=[]
        Fo_hands=[]
        
    for i in EM+EM_hands:
        bpy.ops.object.empty_add(type='PLAIN_AXES', radius=0.15, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.selected_objects[0].name=i
            
    bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.context.selected_objects[0].name="mOtioNcaTcH"
    bpy.context.selected_objects[0].data.name="mOtioNcaTcH"
    bpy.ops.armature.select_all(action='SELECT')
    bpy.ops.armature.duplicate_move()
    bpy.context.selected_bones[0].name="数值控制"
    bpy.ops.armature.select_all(action='INVERT')
    #print(bpy.context.selectedbones)
    for i in ['body_bot','head','L_arm_top','L_arm_bot','R_arm_top','R_arm_bot','L_leg_top','L_leg_bot','R_leg_top','R_leg_bot']:
        bpy.context.selected_bones[0].name=i
        #print(bpy.context.selected_bones[0].name)
        bpy.ops.object.mode_set(mode='POSE')
        if i == 'head':
            bpy.data.objects["mOtioNcaTcH"].pose.bones[i].constraints.new("DAMPED_TRACK").target=bpy.data.objects[Tr_group[Co]]
        if i == 'body_bot':
            bpy.data.objects["mOtioNcaTcH"].pose.bones[i].constraints.new("COPY_LOCATION").target=bpy.data.objects[Fo_group[Co]]
        else:
            bpy.data.objects["mOtioNcaTcH"].pose.bones[i].constraints[1].target=bpy.data.objects[Tr_group[Co]]
            bpy.data.objects["mOtioNcaTcH"].pose.bones[i].constraints[0].target=bpy.data.objects[Fo_group[Co]]
        bpy.ops.object.mode_set(mode='EDIT')
        if not i in ['R_leg_bot','body_bot']:
            if i=='L_arm_top':
                bpy.ops.transform.rotate(value=3.14159, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)))
            bpy.ops.armature.duplicate_move()

        elif i== 'body_bot':
            bpy.ops.transform.rotate(value=3.14159, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)))
            bpy.ops.armature.extrude_move()
            bpy.ops.armature.select_more()
            bpy.context.selected_bones[0].name="body_mid"
            bpy.ops.object.mode_set(mode='POSE')
            bpy.data.objects["mOtioNcaTcH"].pose.bones["body_mid"].constraints.new("IK").target=bpy.data.objects[Tr_group[Co]]
            bpy.data.objects["mOtioNcaTcH"].pose.bones["body_mid"].constraints[0].chain_count=2
            bpy.ops.pose.select_all(action='DESELECT')
            bpy.context.object.data.bones['body_bot'].select=True
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.armature.duplicate_move()
        Co+=1
        
    for c,i in enumerate(Fo_hands):
        if c%3==0:
            bpy.ops.armature.bone_primitive_add()
        else:
            bpy.ops.armature.select_less()
            bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value":(0, 0, 1),"orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1))})
        bpy.ops.armature.select_more()
        bpy.context.selected_bones[0].name=i
        bpy.context.selected_bones[0].use_connect=False
        bpy.ops.object.mode_set(mode='POSE')
        bpy.data.objects["mOtioNcaTcH"].pose.bones[i].constraints.new("COPY_LOCATION").target=bpy.data.objects[Fo_hands[c]]
        bpy.data.objects["mOtioNcaTcH"].pose.bones[i].constraints.new("DAMPED_TRACK").target=bpy.data.objects[Tr_hands[c]]
        bpy.ops.object.mode_set(mode='EDIT')
        
    for i in ["L_leg_bot","R_leg_bot","L_leg_top","R_leg_top"]:
        qe=bpy.data.objects["mOtioNcaTcH"].pose.bones[i].constraints
        Ob=qe[len(qe)-1].target
        qe[len(qe)-1].target=bpy.data.objects['body_bot']
        if i in ["L_leg_top","R_leg_top"]:
            pass
            #qe[len(qe)-1].track_axis='TRACK_NEGATIVE_Y'
        qe.new("DAMPED_TRACK").target=Ob
        
    bpy.ops.object.mode_set(mode='POSE')
    qe=bpy.data.objects["mOtioNcaTcH"].pose.bones['body_bot'].constraints.new("DAMPED_TRACK")
    qe.target=bpy.data.objects['L_leg_top']
    qe.track_axis='TRACK_NEGATIVE_X'
    bpy.data.objects["mOtioNcaTcH"].pose.bones['head'].constraints[1].target=bpy.data.objects['nose']
    bpy.data.objects["mOtioNcaTcH"].pose.bones['head'].constraints[1].track_axis='TRACK_NEGATIVE_Z'
    bpy.data.objects["mOtioNcaTcH"].pose.bones['head'].constraints.new("DAMPED_TRACK").target=bpy.data.objects['head_top']
    bpy.data.armatures["mOtioNcaTcH"].bones.active=bpy.data.armatures["mOtioNcaTcH"].bones["数值控制"]
    bpy.ops.pose.select_all(action='SELECT')
    bpy.context.object.data.bones["body_mid"].select=False
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.armature.parent_set(type='OFFSET')
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.empty_add(type='SPHERE', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.context.selected_objects[0].name="动捕父级"
    for i in EM+["mOtioNcaTcH"]+EM_hands:
        bpy.data.objects[i].parent=bpy.data.objects["动捕父级"]
        bpy.data.objects[i].select_set(True)
    bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name="Body_Track_Empty_And_Bones")
    bpy.data.objects["mOtioNcaTcH"].pose.bones["数值控制"]["IK_Control"]=0.3
    bpy.data.objects["动捕父级"]["Z_mu"]=[3.0,1,1]
    for i in range(3):
        sc_dr=bpy.data.objects["mOtioNcaTcH"].pose.bones['body_bot'].driver_add("scale",i)
        sc_dr.driver.use_self=True
        sc_dr.driver.expression="self.parent['IK_Control']"
    
class MOTIONCATCH_MT_error_menu(bpy.types.Menu):
    bl_label = "错误"
    bl_idname = "MOTIONCATCH_MT_error_menu"

    def draw(self, context):
        layout = self.layout
        layout.label(text=bpy.context.scene.Motion_catch.error_thing,icon="ERROR")

    def draw_item(self, context):
        layout = self.layout
        layout.menu(MOTIONCATCH_MT_error_menu.bl_idname)
def rl(naming=MOTIONCATCH_MT_error_menu):
    bpy.ops.wm.call_menu(name=naming.bl_idname)
    
class Motion_catch(bpy.types.Operator):
    bl_idname = "motioncatch.view"
    bl_label = "动捕"
    
    def modal(self, context, event):
        Is_return = 0
        if event.type == 'TIMER':
            Is_return=motion_catch()
        
        if Is_return or event.type == 'LEFTMOUSE':
            cv2.destroyAllWindows()
            self.cancel(context)
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}
        
    def invoke(self, context, event):
        global T1,T2,times,source,Mpose,pose,Mdraw,Count,avg,nor,tools,mf,per_fps,mF,mh,mH
        tools=bpy.context.scene.Motion_catch
        try:
            if tools.Is_Face:
                brEaKEr=bpy.context.scene.Motion_catch_fa_defa
        except:
            bpy.context.scene.Motion_catch.error_thing='面捕未选择预设'
            rl()
            return {"FINISHED"}
        T1,T2=0,0
        times=3
        Count=0
        source = cv2.VideoCapture(tools.Folder)
        if not source.read()[0]:
            tools.error_thing='导入视频出错，请重新选择或手动输入路径'
            rl()
            return {"FINISHED"}
        per_fps=source.get(cv2.CAP_PROP_FPS)
        mF=m.solutions.face_mesh
        mf=mF.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)
        Mpose = m.solutions.pose
        pose=Mpose.Pose()
        mH=m.solutions.hands
        mh=mH.Hands()
        Mdraw = m.solutions.drawing_utils
        avg = lambda a,b,re_b: ((a.x+b.x)/2-re_b[0],(a.z+b.z)/2-re_b[1],(a.y+b.y)/2-re_b[2])
        nor = lambda a,re_b: (a.x-re_b[0],a.z-re_b[1],a.y-re_b[2])
        if tools.Is_Face:
            face_spawn_cache()
        if tools.Is_body:
            body_spawn_cache()

        self._timer = context.window_manager.event_timer_add(1/24, window=context.window)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
        
    def cancel(self, context):
        context.window_manager.event_timer_remove(self._timer)
        if tools.Is_body:
            body=['body_bot','body_top_h_b','head_top','L_arm_top','L_arm_mid','L_arm_bot','R_arm_top','R_arm_mid','R_arm_bot','L_leg_top','L_leg_mid','L_leg_bot','R_leg_top','R_leg_mid','R_leg_bot','nose']
            if tools.Is_hands_catch:
                hands=['1_1', '1_2', '1_3', '1_4', '2_1', '2_2', '2_3', '2_4', '3_1', '3_2', '3_3', '3_4', '4_1', '4_2', '4_3', '4_4', '5_1', '5_2', '5_3', '5_4', '6_1', '6_2', '6_3', '6_4', '7_1', '7_2', '7_3', '7_4', '8_1', '8_2', '8_3', '8_4', '9_1', '9_2', '9_3', '9_4', '10_1', '10_2', '10_3', '10_4']
            else:
                hands=[]
            for i in body+hands:
                for o in range(3):
                    Z=bpy.data.objects[i].driver_add("location",o)
                    Z.driver.use_self=True
                    exec(f"Z.driver.expression=\"self.location[{o}]*self.parent['Z_mu'][{o}]\"")
                    bpy.data.objects["动捕父级"].rotation_euler[0]=3.2183
                    bpy.data.objects["动捕父级"].rotation_euler[1]=-0.0254
                    bpy.data.objects["动捕父级"].rotation_euler[2]=3.1237
        if tools.Is_Face:
            for i in FAEM():
                bpy.data.objects[i]['add']=[0.0,0.0,0.0]
                bpy.data.objects[i]["view_bone_axis"]=[0,1,2]
                bpy.data.objects[i]["view_bone_mul"]=[1.0,1,1]
                for o in range(3):
                    Z=bpy.data.objects[i].driver_add("location",o)
                    Z.driver.use_self=True
                    exec(f"Z.driver.expression=\"(self.location[self[\\\"view_bone_axis\\\"][{o}]]*self[\\\"view_bone_mul\\\"][{o}]+self[\'add\'][{o}])*self.parent[\'mu\'][{o}]+self.parent[\'add\'][{o}]\"")

def cons_add_rem(g,bovar):
    Mo_ca=bpy.context.scene.Motion_catch
    exec(f'global inname,befname;inname=Mo_ca.{bovar};befname=Mo_ca.r_{bovar}')
    aR_need=Mo_ca.Ar_need
    aR_needed=Mo_ca.Ar_needed
    try:
        c=aR_need.pose.bones[inname].constraints.new("COPY_ROTATION")
        c.target=aR_needed
        c.subtarget=bovar
        c.mix_mode="BEFORE"
        c.target_space="LOCAL"
        c.owner_space="LOCAL"
        c=aR_need.pose.bones[inname].constraints.new("COPY_LOCATION")
        c.target=aR_needed
        c.subtarget=bovar
        c.target_space="LOCAL"
        c.owner_space="LOCAL"
        c.use_offset=Mo_ca.Is_use_offset
    except:
        pass
    try:
        rem_bo_con=g.pose.bones[befname].constraints
        rem_bo_con.remove(rem_bo_con[len(rem_bo_con)-1])
        rem_bo_con.remove(rem_bo_con[len(rem_bo_con)-1])
    except:
        pass
    exec(f'Mo_ca.r_{bovar}=Mo_ca.{bovar}')

def Ar_se_er(self, context):
    Mo_ca=bpy.context.scene.Motion_catch
    if not Mo_ca.Ar_needed is None:
        a=Mo_ca.Ar_needed.pose
        if a is None:
            bpy.context.scene.Motion_catch.error_thing='此物体没有骨骼'
            rl()
            Mo_ca.Ar_needed=Mo_ca.re_Ar_needed
        else:
            try:
                vv=Mo_ca.Ar_needed['Is_Facecatch(Don\'t touch it!)']
            except:
                bpy.context.scene.Motion_catch.error_thing='此物体不是已被面捕骨骼'
                rl()
                Mo_ca.Ar_needed=Mo_ca.re_Ar_needed
    else:
        a=0
    if not Mo_ca.Ar_need is None:
        a=Mo_ca.Ar_need.pose
        if a is None:
            bpy.context.scene.Motion_catch.error_thing='此物体没有骨骼'
            rl()
            Mo_ca.Ar_need=Mo_ca.re_Ar_need
    else:
        a=0
    if Mo_ca.Ar_needed==Mo_ca.Ar_need and not Mo_ca.Ar_need is None and bool(a):
        bpy.context.scene.Motion_catch.error_thing='为什么要给予一样的物体呢？（出了问题不负责哈(￣◇￣;)┐'
        rl()
    if Mo_ca.Ar_need!=Mo_ca.re_Ar_need and not a is None:
        #View_mode=bpy.context.mode
        #bpy.ops.object.mode_set(mode='POSE')
        aR_need=Mo_ca.Ar_need
        aR_needed=Mo_ca.Ar_needed
        re_aR_need=Mo_ca.re_Ar_need
        for bovar in FABO():
            cons_add_rem(re_aR_need,bovar)
        Mo_ca.re_Ar_need=Mo_ca.Ar_need
        #bpy.ops.object.mode_set(mode=View_mode)
    if Mo_ca.Ar_needed!=Mo_ca.re_Ar_needed and bool(a):
        aR_need=Mo_ca.Ar_need
        aR_needed=Mo_ca.Ar_needed
        for bovar in FABO():
            try:
                exec(f"c=aR_need.pose.bones[Mo_ca.{bovar}].constraints;c[len(c)-1].target=ar_needed;c[len(c)-1].subtarget={bovar};c[len(c)-2].target=aR_needed;c[len(c)-2].subtarget={bovar}")
            except:
                pass
        Mo_ca.re_Ar_needed=Mo_ca.Ar_needed
def bocons(self, context):
    Mo_ca=bpy.context.scene.Motion_catch
    aR_need=Mo_ca.Ar_need
    aR_needed=Mo_ca.Ar_needed
    for bovar in FABO():
        exec(f'if Mo_ca.{bovar}!=Mo_ca.r_{bovar}:cons_add_rem(aR_need,bovar)')
    

def Use_offset(self, context):
    Mo_ca=bpy.context.scene.Motion_catch
    aR_need=Mo_ca.Ar_need
    aR_needed=Mo_ca.Ar_needed
    for i in FABO():
        exec(f'''try:c=aR_need.pose.bones[Mo_ca.{i}].constraints;c[len(c)-1].use_offset=Mo_ca.Is_use_offset\nexcept:pass''')
    

def Vi(self, context):
    Mo_ca=bpy.context.scene.Motion_catch
    aR_need=Mo_ca.Ar_need
    aR_needed=Mo_ca.Ar_needed
    #View_mode=bpy.context.mode
    #bpy.ops.object.mode_set(mode='POSE')
    for i in FABO():
        exec(f'''try:c=aR_need.pose.bones[Mo_ca.{i}].constraints;c[len(c)-1].enabled=Mo_ca.Is_Vi;c[len(c)-2].enabled=Mo_ca.Is_Vi\nexcept:pass''')
    #bpy.ops.object.mode_set(mode=View_mode)

class face_bake(bpy.types.Operator):
    bl_idname = "motioncatch.face_bake"
    bl_label = "面捕动作烘焙"
    def execute(self,context):
        Mo_ca=bpy.context.scene.Motion_catch
        aR_need=Mo_ca.Ar_need
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active=aR_need
        aR_need.select_set(True)
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='DESELECT')
        for i in FABO():
            try:
                exec(f"aR_need.pose.bones[Mo_ca.{i}].bone.select=True")
            except:
                pass
        bpy.ops.nla.bake(frame_start=bpy.context.scene.frame_start,
            frame_end=bpy.context.scene.frame_end,
            step=Mo_ca.bake_step,
            only_selected=True,
            visual_keying=True,
            clear_constraints=True,
            clear_parents=Mo_ca.clear_parents,
            use_current_action=Mo_ca.use_current_action,
            clean_curves=Mo_ca.clean_curves)
        return {"FINISHED"}
                
class Vars(bpy.types.PropertyGroup):
     
    bo_Var=FABO()
    bo_Name=['左眉毛','右眉毛','左眼上部','右眼上部','嘴左部','嘴右部','嘴上部','嘴下部','左眼球','右眼球']
    
    bake_step:IntProperty(
        name ='烘焙步数',
        default = 1)
    clear_parents:BoolProperty(
        name ='清除父极',
        description='将动画烘焙到物体上，然后清除父级(仅对象)',
        default = 0)
    use_current_action:BoolProperty(
        name ='覆盖当前动作',
        description='将动画烘焙到当前动作中，而不是创建一个新的动作',
        default = 0)
    clean_curves:BoolProperty(
        name ='清除曲线',
        description='烘焙曲线后，移除冗余关键帧',
        default = 0)
    
    Folder: StringProperty(
        name="视频文件路径",
        subtype='FILE_PATH',
        default="")
        
    Folder_fd: StringProperty(
        name="面部图片文件路径",
        description="想要被捕捉预设的图片的路径",
        subtype='FILE_PATH',
        default="")
    img_fd_name: StringProperty(
        name="预设名称",
        description="想要创建的预设的名称",
        default="")
        
    Is_show_Face:BoolProperty(
        name ='展开面捕所有选项',
        default = 0)
        
    Is_Face:BoolProperty(
        name ='面部动作捕捉',
        default = 1)
    Is_ShowFaceline:BoolProperty(
        name ='展示面部动捕线',
        default = 1)
    Is_ShowFace:BoolProperty(
        name ='展示面部动捕点',
        description='(注:可能会降低帧率)',
        default = 0)
    Is_ShowFaceEdge:BoolProperty(
        description='(注:可能会降低帧率)',
        name ='展示面部主体轮廓',
        default = 0)
    Is_ShowBones:BoolProperty(
        name ='展示骨骼对照',
        description="是否展示面部骨骼对照",
        default = 0)
           
    show_face_bones_presets: BoolProperty(
        name="展示面捕骨骼映射预设",
        default = 0)
           
    Ar_needed:PointerProperty(type=bpy.types.Object,
        name="已被面捕",
        description="已被面捕骨骼所在的物体",
        update=Ar_se_er)
    Ar_need:PointerProperty(type=bpy.types.Object,
        name='需面捕',
        description="需面捕动画的骨骼所在的物体",
        update=Ar_se_er)
    re_Ar_need:PointerProperty(type=bpy.types.Object,name=" 需面捕")
    re_Ar_needed:PointerProperty(type=bpy.types.Object,name="已被面捕")
    
    Is_hands_catch: BoolProperty(
        name="手部动捕",
        description="只能出现两只手！",
        default = 0)
    
    Is_use_offset:BoolProperty(
        name="位置偏移量",
        description ='开启“复制位置”修改器的"偏移量"选项',
        default = 0,
        update=Use_offset)
    Is_Vi:BoolProperty(
        name="修改可见",
        description ='开启/关闭 骨骼约束修改器可见',
        default = 1,
        update=Vi)
        
    for i in range(len(bo_Var)):
        bovar=bo_Var[i]
        boname=bo_Name[i]
        exec(f'{bovar}:StringProperty(name=\"  {boname}\",update=bocons);r_{bovar}:StringProperty(name=\"{boname}\")')
    
    Is_body:BoolProperty(
        name ='身体动作捕捉',
        default = 1)
        
    Is_align_framend:BoolProperty(
        name = '结束点对齐',
        description = '当动捕时间大于时间结束点时\n使时间结束点对齐捕捉结束点',
        default = 1)
        
    error_thing:StringProperty(
        name="error",
        default="")

class Vars1(bpy.types.PropertyGroup):
    for i in FABO():
        exec(f'pa_lo_{i}:FloatVectorProperty(name=\"{i}\",default=[0,0,0])')
        exec(f'pa_ro_{i}:FloatVectorProperty(name=\"{i}\",default=[0,0,0])')
    for i in FAEM():
        exec(f'pa_lo1_{i}:FloatVectorProperty(name=\"{i}\",default=[0,0,0])')
        exec(f'pa_mu1_{i}:FloatVectorProperty(name=\"{i}\",default=[1,1,1])')
        exec(f'pa_map1_{i}:IntVectorProperty(name=\"{i}\",default=[0,1,2])')
    pa_all_lo:FloatVectorProperty(name='1',default=[0,0,0])
    pa_all_mu:FloatVectorProperty(name='2',default=[1,1,1])
    
    preset_name:StringProperty(name='预设名称')

class ex_pr_add(bpy.types.Operator):
    bl_idname = "motioncatch.ex_pr_add"
    bl_label = "捕捉为预设"  
    bl_description = "记录选中面部父级所对的基本所有自定义选项与骨骼的位置与旋转数据，以便下次调用"
    def execute(self,context):
        Mo_ca_pr = context.scene.Mo_ca_pr
        if Mo_ca_pr.preset_name=="":
            bpy.context.scene.Motion_catch.error_thing='未填入预设名称'
            rl()
            return {"FINISHED"}
        try:
            Ch=bpy.context.object.children
            if '面捕空物体父级' in Ch[0].name:
                empar=Ch[0]
                faceCatch=Ch[1]
            else:
                empar=Ch[1]
                faceCatch=Ch[0]
            tT=faceCatch["Is_Facecatch(Don't touch it!)"]
            ChEM=empar.children
        except:
            bpy.context.scene.Motion_catch.error_thing='选择的物体不是面部父级'
            rl()
            return {"FINISHED"}
        for i in FABO():
            Bo=faceCatch.pose.bones[i]
            exec(f"Mo_ca_pr.pa_lo_{i}=Bo.location")
            exec(f"Mo_ca_pr.pa_ro_{i}=Bo.rotation_euler")
        for i in FAEM():
            for o in ChEM:
                if i in o.name:
                    exec(f"Mo_ca_pr.pa_lo1_{i}=o['add']")
                    exec(f"Mo_ca_pr.pa_mu1_{i}=o['view_bone_mul']")
                    exec(f"Mo_ca_pr.pa_map1_{i}=o['view_bone_axis']")
                    break
        Mo_ca_pr.pa_all_lo=empar['add']
        Mo_ca_pr.pa_all_mu=empar['mu']
        bpy.ops.motioncatch.extra_bones_presets(name=Mo_ca_pr.preset_name, remove_name=False, remove_active=False)
        return {"FINISHED"}

class ex_pr_apply(bpy.types.Operator):
    bl_idname = "motioncatch.ex_pr_apply"
    bl_label = "应用预设" 
    def execute(self,context):
        Mo_ca_pr = context.scene.Mo_ca_pr
        try:
            Ch=bpy.context.object.children
            if '面捕空物体父级' in Ch[0].name:
                empar=Ch[0]
                faceCatch=Ch[1]
            else:
                empar=Ch[1]
                faceCatch=Ch[0]
            tT=faceCatch["Is_Facecatch(Don't touch it!)"]
            ChEM=empar.children
        except:
            bpy.context.scene.Motion_catch.error_thing='选择的物体不是面部父级'
            rl()
            return {"FINISHED"}
        for i in FABO():
            Bo=faceCatch.pose.bones[i]
            exec(f"Bo.location=Mo_ca_pr.pa_lo_{i}")
            exec(f"Bo.rotation_euler=Mo_ca_pr.pa_ro_{i}")
        for i in FAEM():
            for o in ChEM:
                if i in o.name:
                    exec(f"o['add']=Mo_ca_pr.pa_lo1_{i}")
                    exec(f"o['view_bone_mul']=Mo_ca_pr.pa_mu1_{i}")
                    exec(f"o['view_bone_axis']=Mo_ca_pr.pa_map1_{i}")
                    break
        empar['add']=Mo_ca_pr.pa_all_lo
        empar['mu']=Mo_ca_pr.pa_all_mu
        return {"FINISHED"}

class ex_pr_rem(bpy.types.Operator):
    bl_idname = "motioncatch.ex_pr_rem"
    bl_label = "移除预设" 
    def execute(self,context):
        bpy.ops.motioncatch.extra_bones_presets(remove_active=True)
        return {"FINISHED"}
    
class MOTIONCATCH_MT_extra_Face_Bones_Presets_menu(bpy.types.Menu):
    bl_label = "面部骨骼其他应用预设"
    bl_idname = "MOTIONCATCH_MT_extra_Face_Bones_Presets_menu"
    bl_description = "调用骨骼其他应用预设的地方"
    preset_subdir = "extra_Face_Bones_default"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset

class Add_extra_Bones_Preset(AddPresetBase, bpy.types.Operator):
    bl_idname = "motioncatch.extra_bones_presets"
    bl_label = "添加骨骼其他应用预设"
    preset_menu = "MOTIONCATCH_MT_extra_Face_Bones_Presets_menu"

    preset_defines = [
        "Mp=bpy.context.scene.Mo_ca_pr"
    ]
    preset_values = [
        "Mp.pa_lo_"+i for i in FABO()]+[
        "Mp.pa_ro_"+i for i in FABO()]+[
        "Mp.pa_lo1_"+i for i in FAEM()]+[
        "Mp.pa_mu1_"+i for i in FAEM()]+[
        "Mp.pa_map1_"+i for i in FAEM()]+[
        "Mp.pa_all_lo",
        "Mp.pa_all_mu"]

    preset_subdir = "extra_Face_Bones_default"

class fd_pe_add(bpy.types.Operator):
    bl_idname = "motioncatch.fa_pe_add"
    bl_label = "捕捉为预设"  
    bl_description = "通过上面的图像路径来识别并保存预设\n(注:有同名项将直接覆盖)"
    def execute(self, context):
        img_fd = cv2.imread(bpy.context.scene.Motion_catch.Folder_fd)
        if img_fd is None:
            bpy.context.scene.Motion_catch.error_thing='导入图片出错，请重新选择或手动输入路径'
            rl()
            return {"FINISHED"}
        elif context.scene.Motion_catch.img_fd_name=='':
            bpy.context.scene.Motion_catch.error_thing='未输入预设名称'
            rl()
            return {"FINISHED"}
        mF=m.solutions.face_mesh
        mf=mF.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)
        imgRGB = cv2.cvtColor(img_fd,cv2.COLOR_BGR2RGB)
        results = mf.process(imgRGB).multi_face_landmarks[0].landmark
        True_results=[[i.x,i.y,i.z] for i in results]
        bpy.types.Scene.Motion_catch_fa_defa=True_results
        Mo_ca = context.scene.Motion_catch
        bpy.ops.motioncatch.presets(name=Mo_ca.img_fd_name, remove_name=False, remove_active=False)
        context.scene.Motion_catch.img_fd_name=''
        return {"FINISHED"}
class fd_pe_rem(bpy.types.Operator):
    bl_idname = "motioncatch.fa_pe_rem"
    bl_label = "删除预设"  
    def execute(self, context):
        Mo_ca = context.scene.Motion_catch
        try:
            bpy.ops.motioncatch.presets(remove_active=True)
            del bpy.types.Scene.Motion_catch_fa_defa
        except:
            pass
        return {"FINISHED"}
    
class real_MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset(bpy.types.Operator):
    bl_idname = "motioncatch.real_res_bones_presets"
    bl_label = "真正重置骨骼选项"
    def execute(self,context):
        for i in FABO():
            exec(f'context.scene.Motion_catch.{i}=\'\'')
        return {"FINISHED"}

class MOTIONCATCH_MT_is_Face_Bones_Presets_Reset_menu(bpy.types.Menu):
    bl_idname = "MOTIONCATCH_MT_is_Face_Bones_Presets_Reset_menu"
    bl_label = "是否真的重置骨骼选项?"
    def draw(self,context):
        layout=self.layout
        layout.operator(real_MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset.bl_idname,text="确定")
    
class MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset(bpy.types.Operator):
    bl_idname = "motioncatch.res_bones_presets"
    bl_label = "重置骨骼选项"
    def execute(self,context):
        bpy.ops.wm.call_menu(name=MOTIONCATCH_MT_is_Face_Bones_Presets_Reset_menu.bl_idname)
        return {"FINISHED"}

class MOTIONCATCH_MT_Face_Bones_Presets_menu(bpy.types.Menu):
    bl_label = "面部骨骼预设"
    bl_idname = "MOTIONCATCH_MT_Face_Bones_Presets_menu"
    bl_description = "调用预设的地方"
    preset_subdir = "Face_Bones_default"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset
class Add_Bones_Preset(AddPresetBase, bpy.types.Operator):
    bl_idname = "motioncatch.bones_presets"
    bl_label = "添加骨骼预设"
    preset_menu = "MOTIONCATCH_MT_Face_Bones_Presets_menu"

    preset_defines = [
        "bp=bpy.context.scene.Motion_catch"
    ]

    preset_values = [
        "bp."+i for i in FABO()
    ]

    preset_subdir = "Face_Bones_default"

class Rem_Bones_Preset(bpy.types.Operator):
    bl_idname = "motioncatch.rem_bones_presets"
    bl_label = "移除骨骼预设"
    def execute(self,context):
        bpy.ops.motioncatch.bones_presets(remove_active=True)
        return {"FINISHED"}

class MOTIONCATCH_MT_face_presets_menu(bpy.types.Menu):
    bl_label = "面部预设"
    bl_idname = "MOTIONCATCH_MT_face_presets_menu"
    bl_description = "调用预设的地方"
    preset_subdir = "Face_image_default"
    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset
class Add_Preset(AddPresetBase, bpy.types.Operator):
    bl_idname = "motioncatch.presets"
    bl_label = "添加面部基本形状"
    bl_description = "面部会以此图为基准进行面捕"
    preset_menu = "MOTIONCATCH_MT_face_presets_menu"

    preset_defines = [
        "sc=bpy.types.Scene"
    ]

    preset_values = [
        "sc.Motion_catch_fa_defa"
    ]

    preset_subdir = "Face_image_default"
    
class MOTIONCATCH_PT_ui_panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Motioncatch"
    bl_idname = "MOTIONCATCH_PT_ui_panel"
    bl_label = "动捕"
    
    def draw(self, context):
        layout = self.layout
        Mo_ca = context.scene.Motion_catch
        layout.prop(Mo_ca,"Folder")
        layout=layout.column().box().column(align=True)
        layout.label(text="面捕")
        box1 = layout.column().box()
        box1.enabled=bool(context.scene.Motion_catch.Folder)
        box1.prop(Mo_ca,"Is_Face",icon='CHECKBOX_HLT' if Mo_ca.Is_Face else 'CHECKBOX_DEHLT')
        box1.prop(Mo_ca,'Is_show_Face',icon="TRIA_DOWN" if Mo_ca.Is_show_Face else "TRIA_RIGHT")
        if Mo_ca.Is_show_Face:
            col=box1.column().column(align=True)
            col.prop(Mo_ca,'Is_ShowFaceline')
            col.prop(Mo_ca,"Is_ShowFace")
            col.prop(Mo_ca,"Is_ShowFaceEdge")
            split = layout.split()
            box=split.box()
            bocol = box.column()
            bocol.label(text="· 面部预设")
            bocol.prop(Mo_ca,"Folder_fd")
            box=bocol.row(align=True)
            box.enabled=bool(context.scene.Motion_catch.Folder_fd)
            box.prop(Mo_ca,"img_fd_name")
            box.operator(fd_pe_add.bl_idname, text="", icon='ADD')
            borow=bocol.row(align=True).row()
            borow.menu(MOTIONCATCH_MT_face_presets_menu.__name__, text=MOTIONCATCH_MT_face_presets_menu.bl_label, translate=False, icon='PRESET')
            borow.operator(fd_pe_rem.bl_idname, text="", icon='REMOVE')
            box=layout.column().box().column()
            box.label(text="· 面部骨骼应用")
            if Mo_ca.Is_ShowBones:
                box.prop(Mo_ca,'Is_ShowBones',icon="TRIA_DOWN")
                box.prop(Mo_ca,'Ar_needed')
                box.prop(Mo_ca,'Ar_need')
                for i in ['le_br','ri_br','le_eye','ri_eye','le_eyeb','ri_eyeb','le_mouse','ri_mouse','top_mouse','bot_mouse']:
                    try:
                        box.prop_search(Mo_ca,i,Mo_ca.Ar_need.pose,'bones',icon='BONE_DATA')
                    except:
                        pass
                if bool(Mo_ca.Ar_need):
                    bor=box.row(align=True)
                    bor.prop(Mo_ca,'Is_Vi')
                    bor.prop(Mo_ca,'Is_use_offset')
                box2=box.row(align=True)
                box2.menu(MOTIONCATCH_MT_Face_Bones_Presets_menu.__name__, text=MOTIONCATCH_MT_Face_Bones_Presets_menu.bl_label, translate=False, icon='PRESET')
                box2.operator(Add_Bones_Preset.bl_idname, text="", icon='ADD')
                box2.operator(Rem_Bones_Preset.bl_idname, text="", icon='REMOVE')
                box3=box.column()
                box3.enabled=bool(Mo_ca.Ar_need)
                box3.operator(MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset.bl_idname,icon='LOOP_BACK')
                box4=box.column().column()
                box4.label(text="·  烘焙")
                box4.enabled=bool(Mo_ca.Ar_needed) and bool(Mo_ca.Ar_need)
                box4.operator(face_bake.bl_idname)
                if bool(Mo_ca.Ar_needed) and bool(Mo_ca.Ar_need):
                    box5=box.column().column(align=True)
                    box5.prop(Mo_ca,'bake_step')
                    box5.prop(Mo_ca,'clear_parents')
                    box5.prop(Mo_ca,'use_current_action')
                    box5.prop(Mo_ca,'clean_curves')
                
            else:
                box.prop(Mo_ca,'Is_ShowBones',icon="TRIA_RIGHT")
            Mo_ca_pr=context.scene.Mo_ca_pr
            boxu=layout.column().box()
            boxuct=boxu.column(align=True)
            boxuct.label(text='·面捕骨骼参数预设应用')
            boxuct.prop(Mo_ca,"show_face_bones_presets",icon="TRIA_DOWN" if Mo_ca.show_face_bones_presets else "TRIA_RIGHT")
            if Mo_ca.show_face_bones_presets:
                boxe=boxu
                boxee=boxe.column(align=True)
                try:
                    boxee.label(text="已激活的物体:"+context.object.name)
                    Ch=bpy.context.object.children
                except:
                    boxee.label(text="已激活的物体:")
                try:
                    if '面捕空物体父级' in Ch[0].name:
                        empar=Ch[0]
                        faceCatch=Ch[1]
                    else:
                        empar=Ch[1]
                        faceCatch=Ch[0]
                    tT=faceCatch["Is_Facecatch(Don't touch it!)"]
                except:
                    if not context.object is None:
                        boxee.label(text='注:选择的物体不是面部父级,无法使用')
                boxgg=boxe.column(align=True)
                boxggg=boxgg.row()
                boxggg.prop(Mo_ca_pr,'preset_name')
                boxggg.operator(ex_pr_add.bl_idname, text="", icon='ADD')
                boxgggg=boxgg.row()
                boxgggg.menu(MOTIONCATCH_MT_extra_Face_Bones_Presets_menu.__name__, text=MOTIONCATCH_MT_extra_Face_Bones_Presets_menu.bl_label, translate=False, icon='PRESET')
                boxgggg.operator(ex_pr_rem.bl_idname, text="", icon='REMOVE')
                boxGggg=boxe.column()
                boxGggg.operator(ex_pr_apply.bl_idname)
            
        layout.label(text="动捕")
        boxr=layout.column().box()
        boxr.enabled=bool(context.scene.Motion_catch.Folder)
        boxr.prop(Mo_ca,"Is_body",icon='CHECKBOX_HLT' if Mo_ca.Is_body else 'CHECKBOX_DEHLT')
        boxr.prop(Mo_ca,"Is_hands_catch")
        
        layout = self.layout
        layout.prop(Mo_ca,'Is_align_framend')
        
        split = layout.split()
        col = split.column(align=True)
        if (Mo_ca.Is_Face or Mo_ca.Is_body) and bool(Mo_ca.Folder):
            col.enabled=True
        else:
            col.enabled=False
        col.operator('motioncatch.view')

cls_all=(Motion_catch,
    fd_pe_add,
    fd_pe_rem,
    MOTIONCATCH_MT_face_presets_menu,
    Add_Preset,
    MOTIONCATCH_PT_ui_panel,
    Add_Bones_Preset,
    Rem_Bones_Preset,
    MOTIONCATCH_MT_Face_Bones_Presets_menu,
    MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset,
    real_MOTIONCATCH_MT_Face_Bones_Presets_menu_Reset,
    MOTIONCATCH_MT_is_Face_Bones_Presets_Reset_menu,
    face_bake,
    ex_pr_add,
    ex_pr_apply,
    ex_pr_rem,
    MOTIONCATCH_MT_extra_Face_Bones_Presets_menu,
    Add_extra_Bones_Preset,
    MOTIONCATCH_MT_error_menu,
    Install,
    ins_in_pref)
var=(Vars,Vars1)
    
def register():
    for v in var:
        bpy.utils.register_class(v)
    bpy.types.Scene.Motion_catch=bpy.props.PointerProperty(type=Vars)
    bpy.types.Scene.Mo_ca_pr=bpy.props.PointerProperty(type=Vars1)
    if bpy.types.Scene.Motion_catch_isInstall:
        cls=cls_all
    else:
        cls=(Install,ins_in_pref)
    for Class in cls:
        bpy.utils.register_class(Class)
    
def unregister():
    if bpy.types.Scene.Motion_catch_isInstall:
        cls=cls_all
    else:
        cls=(Install,ins_in_pref)
    for Class in cls:
        bpy.utils.unregister_class(Class)
    del bpy.types.Scene.Motion_catch
    del bpy.types.Scene.Mo_ca_pr
    
if __name__=="__main__":
    register()