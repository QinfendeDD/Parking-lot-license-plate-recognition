import datetime
# 计算停车时间四舍五入
def DtCalc(stTime, edTime):
    st=datetime.datetime.strptime(stTime, "%Y-%m-%d %H:%M")
    ed=datetime.datetime.strptime(edTime, "%Y-%m-%d %H:%M")
    rtn = ed -st
    y=round(rtn.total_seconds()/60/60)
    # 判断停车时间 如果时间
    if y == 0:
        y = 1
    return y

# 返回 星期几标记 0代表星期一 1代表星期二...6代表星期天
def get_week_numbeer(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
    day = date.weekday()
    return day