# coding=gbk
s="����"
s1=u"����"
s2=unicode(s,"gbk")
s3=s.decode("gbk")
print len(s1)
print len(s2)
print len(s3)