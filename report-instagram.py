ó
7éÀ`c           @   s|  d  Z  d Z d Z d Z d d l m Z m Z d d l m Z d d l m	 Z	 d d l
 m Z m Z d d	 l
 m Z m Z m Z d d
 l
 m Z m Z m Z d d l
 m Z m Z m Z d d l m Z g  Z g  Z d   Z d   Z e d k rxe   e d  e d  Z e d  e d  Z d GHe d  Z e d  Z e d  Z e d k rce  Z n) e d k rxe! Z n e d  e" d  e d  Z# e# d k r­e  Z# n) e# d k rÂe! Z# n e d  e" d  e   e d  Z$ d GHe d  d GHe# e! k re   qxxb e D]W Z% e	 d e d  e e e% d! e% d" e e! k rRd# n	 e e  e$ f  Z' e' j(   qWn  d# S($   s   Marwan 007 : @mrwn.007t   GPLv3s   0.1s   being developediÿÿÿÿ(   t   timet   sleep(   t   choice(   t   Process(   t   CheckPublicIPt   IsProxyWorking(   t   PrintStatust   PrintSuccesst
   PrintError(   t   PrintBannert   GetInputt   PrintFatalError(   t	   LoadUserst   LoadProxiest   PrintChoices(   t   InstaClientc         C   s¡   d  } | d  k rG t d | d d  t | | | d | d  } n* t d | d d  t | | d  d   } | j   | j   | j | |  |  d GHd  S(   Nt   [t   ]s   Logging into the Account!t   ipt   portt    (   t   NoneR   R   t   Connectt   Logint   Spam(   t   usernamet   useridt	   loginusert	   loginpasst   proxyt   reasonidt   client(    (    s.   /storage/emulated/0/Movies/report-instagram.pyt   MultiThread"   s$    	

c          C   sÜ   xÕ t  D]Í }  d  } t rf t t  } t d |  d d d  t |  d |  d | d | d  } nB t t  } t d |  d d d  t |  d |  d d  d   } | j   | j   | j	 t
 t t  d GHq Wd  S(	   NR   t   userR   s   Logging into the Account!t   passwordR   R   R   (   t   USERSR   t   useproxyR   t   PROXIESR   R   R   R   R   R   R   R   (   R"   R    R   (    (    s.   /storage/emulated/0/Movies/report-instagram.pyt   NoMultiThread:   s*    	

t   __main__s   Loading users!s   ./users.txts   Loading Proxes!s   ./proxy.txtR   s0   The account username you want to complain about:s.   The account number you want to complain about:s#   Do you want to use proxy? [Yes No]:t   Yest   Nos    Please just enter 'Yes' or 'No'!i    s   Do you want to use multithreading? [Yes / No] (Do not use this feature if you have too many users or if your computer is slow!):sJ   Please select one of the reasons for the above complaint (ex: 1 for spam):s	   Starting!t   targett   argsR"   R#   N()   t
   __author__t   __license__t   __version__t
   __status__R   R   t   randomR   t   multiprocessingR   t
   libs.utilsR   R   R   R   R	   R
   R   R   R   R   R   t   libs.instaclientR   R$   R&   R!   R'   t   __name__R   R   R%   t   Truet   Falset   exitt   usemultithreadR   R"   R   t   pt   start(    (    (    s.   /storage/emulated/0/Movies/report-instagram.pyt   <module>   sl   		

		

		



