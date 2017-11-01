function GetDateTimeDiff(startTime, endTime) {
    var retValue = {};

    var date3 = endTime.getTime() - startTime.getTime();  //时间差的毫秒数

    //计算出相差天数
    var days = Math.floor(date3 / (24 * 3600 * 1000));
    retValue.Days = days;

    var years = Math.floor(days / 365);
    retValue.Years = years;

    var months = Math.floor(days / 30);
    retValue.Months = months;

    //计算出小时数
    var leave1 = date3 % (24 * 3600 * 1000);    //计算天数后剩余的毫秒数
    var hours = Math.floor(leave1 / (3600 * 1000));
    retValue.Hours = hours;

    //计算相差分钟数
    var leave2 = leave1 % (3600 * 1000);        //计算小时数后剩余的毫秒数
    var minutes = Math.floor(leave2 / (60 * 1000));
    retValue.Minutes = minutes;

    //计算相差秒数
    var leave3 = leave2 % (60 * 1000);      //计算分钟数后剩余的毫秒数
    var seconds = Math.round(leave3 / 1000);
    retValue.Seconds = seconds;

    var strTime = "";
    if (years >= 1) {
        strTime = years + "年前";
    } else if (months >= 1) {
        strTime = months + "个月前";
    } else if (days >= 1) {
        strTime = days + "天前";
    } else if (hours >= 1) {
        strTime = hours + "小时前";
    } else {
        strTime = minutes + "分钟前";
    }
    retValue.PubTime = strTime;     //帖子,文章,博客发表时间的一种简短表示方法
    // return retValue;
    return 100;
}