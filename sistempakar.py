from flask import Flask, session, redirect, url_for, render_template, request, escape
app = Flask(__name__)
app.secret_key = 'isinya password buat session'
app.static_folder = 'static'

daftarGejala = ['Gigi terasa ngilu','Gigi terasa berdenyut','Kepala terasa pusing','Terdapat lubang pada gigi','Gusi bengkak','Demam (suhu badan diatas 38 derajat)','Bau mulut','Gusi berwarna merah tua','Gusi rentan berdarah','Adanya plak/karang gigi','Mulut terasa kering','Sering dehidrasi','Lapisan lidah terasa tebal','Cairan ludah berkurang','Adanya benjolan putih/abu','Terasa luka dan pedih','Gigi terasa sakit','Sakit saat mengunyah','Gigi terasa sensitive','Bentuk gigi tampak terkikis','Gigi terasa nyeri saat makan/minum panas dan dingin','Ngilu berkepanjangan (pada gigi)','Gusi menurun','Sakit setelah pencabutan gigi','Sakit sampai kepala,telinga,mata,leher','Gigi tidak sejajar','Perubahan pada wajah','Tidak nyaman ketika ngunyah dan menggigit','Merasa tidak enak pada mulut','Gigi longgar','Lidah membesar','Nyeri pada lidah','Perubahaan warna pada lidah','Permukaan ldah licin','Warna permukaan lidah kemerahan','Gigi terlihat jarang- jarang','Gigi terlihat tonggos kedepan','Ukuran gigi dan rahan tidak sesuai','Adanya bercak pada sudut bibir','Bercak terasa gatal nyeri dan panas pada bibir','Bila di raba, bercak terasa keras pada bibir','Kadang bercak juga bisa berdarah pada bibir','Cadel','Gigi sulung copot sebelum waktunya (prematur)']
daftarPenyakit = ['Karies gigi (gigi berlubang)','Gingvitis (radang gusi)','Lidah putih','Stomatitis (sariawan)','Abses gigi (gusi bengkak/nanah)','Abrasi gigi (hilangnya struktur gigi)','Gigi sensitive','Alveolar osteitis (peradangan)','Maloklusi (gigi berdesakan)','Resesi gusi (penurunan gusi)','Gloositis (radang lidah)','Crowded (gigi berjejal)','Cheilitis (radang bibir)']
solusiPenyakit = ['Tambal Gigi, Perawatan Saluran akar gigi, dan Cabut gigi','Obat pereda nyeri,Obat kumur, dan Obat antibiotik','Minum banyak air untuk membantu menghilangkan bakteri dan Menyikatnya dengan pembersih lidah khusu','Pengobatan stomatitis aftosa,Pengobatan stomatitis herpes','Perawatan saluran akar (root canal),Cabut gigi','Pembuatan Mahkota Gigi (Crown),Penambalan Gigi','Menggosok Gigi dengan benar,Hindari makanan dan minuman asam','Pemberian obat kumur atau gel antibakteri segera sebelum dan sesudah operasi,Pemberian larutan antiseptik diberikan pada luka','Pasang kawat gigi,Cabut gigi','Perawatan dengan scaling dan root planning','Menjaga kesehatan rongga mulut dengan cara menyikat gigi dua kali sehari (setelah sarapan dan sebelum tidur),Perubahan pola makan untuk mengatasi permasalahan nutrisi yang dapat menjadi penyebab terjadinya glositis','Perawatan orthodonsi','Salep anti jamur,Salep antibakteri']
gejala = 0

def checkGejala():
    if request.form.get('pilihan') == 'ya':
        return True
    if request.form.get('pilihan') == 'tidak':
        return False
    else:
        return checkGejala()

@app.route('/')
def index():
   session.pop('namaPasien', None)
   session.pop('gejalaPasien', None)
   session.pop('logs', None)
   session.pop('logs2', None)
   session['gejalaPasien'] = 0
   session['logs'] = 0
   session['logs2'] = 0
   return render_template('index.html', link = url_for('index'))

@app.route('/welcome',methods = ['POST', 'GET'])
def welcome():
   if request.method == 'POST':
      name = request.form.get('Name')
      session['namaPasien'] = name
      gejalanya = session['gejalaPasien']
      pertanyaan = daftarGejala[gejalanya]
      return render_template("welcome.html", name = name,  pertanyaan = pertanyaan, link = url_for('index'))

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      #=============================================================Logs 0
      if session['logs'] == 0 and checkGejala():
         if session['gejalaPasien'] == 0: # Gejala 1
            session['gejalaPasien'] = 1
            session['logs'] = 1
            return redirect(url_for('diagnosa'))

      #=============================================================Logs 1
      elif session['logs'] == 1  and checkGejala():
         if session['gejalaPasien'] == 1: # Gejala 1
            session['gejalaPasien'] = 2
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 5 and session['logs2'] == 0: # Gejala 8
            session['gejalaPasien'] = 6
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 10: # Gejala 3
            session['gejalaPasien'] = 11
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 13: # Gejala 4
            session['gejalaPasien'] = 14
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 25 and session['logs2'] == 0: # Gejala 9
            session['gejalaPasien'] = 26
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 30: # Gejala 11
            session['gejalaPasien'] = 31
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 35: # Gejala 12
            session['gejalaPasien'] = 36
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 38: # Gejala 13
            session['gejalaPasien'] = 39
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 18: # Gejala 6
            session['gejalaPasien'] = 19
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 20: # Gejala 7
            session['gejalaPasien'] = 21
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 25 and session['logs2'] == 1: # Gejala 7
            session['gejalaPasien'] = 28
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 4 and session['logs2'] == 1: # Gejala 2
            session['gejalaPasien'] = 6
            session['logs'] = 2
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 5 and session['logs2'] == 1: # Gejala 5
            session['gejalaPasien'] = 16
            session['logs'] = 2
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))

      #=============================================================Logs 2
      elif session['logs'] == 2 and checkGejala():
         if session['gejalaPasien'] == 2: # Gejala 1
            session['gejalaPasien'] = 3
            session['logs'] = 3
            return redirect(url_for('diagnosa'))  
         elif session['gejalaPasien'] == 6 and session['logs2'] == 0: # Gejala 8
            session['gejalaPasien'] = 16
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 11: # Gejala 3
            session['gejalaPasien'] = 12
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 14: # Gejala 4
            session['gejalaPasien'] = 15
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 26: # Gejala 9
            session['gejalaPasien'] = 27
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 31: # Gejala 11
            session['gejalaPasien'] = 32
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 36: # Gejala 12
            session['gejalaPasien'] = 37
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 39: # Gejala 13
            session['gejalaPasien'] = 40
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 19: # Gejala 6
            session['gejalaPasien'] = 21
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 21: # Gejala 7
            session['gejalaPasien'] = 22
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 28: # Gejala 7
            session['gejalaPasien'] = 29
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 6 and session['logs2'] == 1: # Gejala 2
            session['gejalaPasien'] = 7
            session['logs'] = 3
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 16 and session['logs2'] == 1: # Gejala 5
            session['gejalaPasien'] = 17
            session['logs'] = 3
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))
 

      #=============================================================Logs 3
      elif session['logs'] == 3 and checkGejala():
         if session['gejalaPasien'] == 3: # Gejala 1
            session['gejalaPasien'] = 5
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 16: # Gejala 8
            session['gejalaPasien'] = 23
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 12: # Gejala 3
            session['gejalaPasien'] = 13
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 15: # Gejala 4
            terjangkitPenyakit = daftarPenyakit[3]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[3]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 27: # Gejala 9
            session['gejalaPasien'] = 42
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 32: # Gejala 11
            session['gejalaPasien'] = 33
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 37: # Gejala 12
            session['gejalaPasien'] = 43
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 40: # Gejala 13
            session['gejalaPasien'] = 41
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 21: # Gejala 6
            terjangkitPenyakit = daftarPenyakit[5]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[5]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 22: # Gejala 7
            terjangkitPenyakit = daftarPenyakit[6]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[6]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 29: # Gejala 7
            terjangkitPenyakit = daftarPenyakit[9]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[9]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 7 and session['logs2'] == 1: # Gejala 2
            session['gejalaPasien'] = 8
            session['logs'] = 4
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 17 and session['logs2'] == 1: # Gejala 5
            terjangkitPenyakit = daftarPenyakit[4]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[4]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))

      #=============================================================Logs 4
      elif session['logs'] == 4 and checkGejala():
         if session['gejalaPasien'] == 5: # Gejala 1
            session['gejalaPasien'] = 6
            session['logs'] = 5
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 23: # Gejala 8
            session['gejalaPasien'] = 24
            session['logs'] = 5
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 13: # Gejala 3
            terjangkitPenyakit = daftarPenyakit[2]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[2]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 42: # Gejala 9
            terjangkitPenyakit = daftarPenyakit[8]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[8]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 33: # Gejala 11
            session['gejalaPasien'] = 34
            session['logs'] = 5
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 43: # Gejala 12
            terjangkitPenyakit = daftarPenyakit[11]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[11]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 41: # Gejala 13
            terjangkitPenyakit = daftarPenyakit[12]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[12]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 8 and session['logs2'] == 1: # Gejala 2
            session['gejalaPasien'] = 9
            session['logs'] = 5
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))

      #=============================================================Logs 5
      elif session['logs'] == 5 and checkGejala():
         if session['gejalaPasien'] == 6: # Gejala 1
            session['gejalaPasien'] = 17
            session['logs'] = 6
            return redirect(url_for('diagnosa'))
         if session['gejalaPasien'] == 24: # Gejala 8
            terjangkitPenyakit = daftarPenyakit[7]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[7]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 34: # Gejala 11
            terjangkitPenyakit = daftarPenyakit[10]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[10]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))
         if session['gejalaPasien'] == 9 and session['logs2'] == 1: # Gejala 2
            terjangkitPenyakit = daftarPenyakit[1]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[1]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))

      #=============================================================Logs 6
      elif session['logs'] == 6 and checkGejala():
         if session['gejalaPasien'] == 17: # Gejala 1
            terjangkitPenyakit = daftarPenyakit[0]
            solusiPenyakitnya = "Solusi: " + solusiPenyakit[0]
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, solusiPenyakitnya = solusiPenyakitnya, awal = url_for('index'))

      #=============================================================Logs 1      
      else:
         if session['gejalaPasien'] == 0: # Gejala 8
            session['gejalaPasien'] = 5
            session['logs'] = 1
            session['logs2'] = 0
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 5: # Gejala 3
            session['gejalaPasien'] = 10 
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 10: # Gejala 4
            session['gejalaPasien'] = 13
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 13: # Gejala 9
            session['gejalaPasien'] = 25
            session['logs'] = 1
            session['logs2'] = 0
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 25 and session['logs2'] == 0: # Gejala 11
            session['gejalaPasien'] = 30
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 30: # Gejala 12
            session['gejalaPasien'] = 35
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 35: # Gejala 13
            session['gejalaPasien'] = 38
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 1: # Gejala 6
            session['gejalaPasien'] = 18
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 18: # Gejala 7
            session['gejalaPasien'] = 20
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 19: # Gejala 10
            session['gejalaPasien'] = 25
            session['logs'] = 1
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 25 and session['logs2'] == 1: # Gejala 2
            session['gejalaPasien'] = 4
            session['logs'] = 1
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 7 and session['logs2'] == 1: # Gejala 5
            session['gejalaPasien'] = 5
            session['logs'] = 1
            session['logs2'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 38: # Tidak ada gejala
            terjangkitPenyakit = "Anda tidak terjangkit apapun"
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, awal = url_for('index'))
         else:
            terjangkitPenyakit = "Maaf Sistem kami belum bisa menjawab pertanyaan anda"
            return render_template("result.html", terjangkitPenyakit = terjangkitPenyakit, awal = url_for('index'))
         

@app.route('/diagnosa',methods = ['POST', 'GET'])
def diagnosa():
   name = session['namaPasien']
   pertanyaan = daftarGejala[session['gejalaPasien']]
   return render_template("diagnosa.html", pertanyaan = pertanyaan, name = name, link = url_for('index'))
   
if __name__ == '__main__':
   app.run(debug = True)