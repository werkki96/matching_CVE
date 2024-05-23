def delTrashDatas(df):
    # 설명에 후보가 들어있으면 데이터 삭제
    # ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.
    words = "** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided."
    df = df[~df['Description'].str.contains(words, na = False, regex=False)]

    # 리젝트된 cve면 삭제
    words = "REJECT"
    df = df[~df['Description'].str.contains(words, na = False, regex=False)]
    
    df.to_csv("./allitems_cleaned.csv", index = False)
    print('ok')

# 메인함수, cve 파일 전처리 진행
if __name__ == "__main__":
    import pandas as pd
    read_file = "./allitems.csv"
    try:
        df = pd.read_csv(read_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(read_file, encoding='ISO-8859-1')
    delTrashDatas(df)

#%%
