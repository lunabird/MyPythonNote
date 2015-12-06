# coding=gbk
s="中文"
s1=u"中文"
s2=unicode(s,"gbk")
s3=s.decode("gbk")
print len(s1)
print len(s2)
print len(s3)