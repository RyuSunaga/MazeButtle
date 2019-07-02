#this is client file

##############################################################################################################

#命名規則について by sunaga

# file名　　　　　　　　全て小文字でなるべく短く　       myfile
# クラス名　　　　　　　最初大文字、大文字区切り　　　   ThisIsMyClass
# 関数名、メソッド名　　全小文字、アンダースコア区切り   this_is_my_func
# 変数名　　　　　　　　全小文字、アンダースコア区切り   this_is_my_val
# 定数名                全大文字、アンダースコア区切り　 THIS_IS_MY_CONST

# 自クラス内でのみ使用する内部変数と内部メソッドはアンダースコアで開始


##############################################################################################################


'''
情報の受け渡しについて
辞書型にid,commandを格納    {id,command}

'''

class GamePlayer(object):
    """
    プレイヤーの情報を保持するクラス
    必要情報

    プレイヤー自身の情報
    ------------------------------------------------------------
    1.プレイヤーID             id       int
    2.体力、初期値5            hp       int
    3.位置情報、初期値[,]    place    int_list
    4.攻撃力、初期値2          attack   int
    5.速度、初期値1            speed    int
    ------------------------------------------------------------
    """
    def __init__(self,hp,place,attack,speed):
        self.hp=hp
        self.place=place
        self.attack=attack
        self.speed=speed
        


class Field(object):
    """
    フィールド状況を保持するクラス
    必要情報
    1.プレイヤーらの舞台、MAZE（リスト）
    """

    def __init__(self):
        pass
        
