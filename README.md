# workspace_importer
workspace_importerはスタートアップファイルに保存されているワークスペースをインポートするアドオンです。  
他ユーザーが作成した.blendのワークスペースを、簡単に自分のワークスペースに切り替えることができます。  
<br>
workspace_importer can import Workspace from startup.blend.  
In other's .blend file you can easily use your own Workspace Settings.  
<br>
![アドオン画像](./Doc/workspace_importer.png)
<br>
## 導入方法_Installation
最新版ダウンロードは[こちら](https://github.com/3str6/workspace_importer/blob/master/Doc/workspace_importer.zip)  
1.編集 > プリファレンス... > アドオン > インストール > ダウンロードした.zipを選択します。  
2.下のリストに「User Interface: Workspace Importer」が表示されるのでチェックを入れて有効化します。  
3.3Dビュー > サイドバー（Nキー） > ツール タブ > Workspace Importer　が追加されています。  
<br>
Download from [here](https://github.com/3str6/workspace_importer/blob/master/Doc/workspace_importer.zip)  
1.Edit > Preference... > Add-on > Install > Select the downloaded workspace_importer.zip.  
2.Enable 'User Interface: Workspace Importer'.  
3.View3d > Sidebar(N-key) > Tool Tab > Workspace Importer Panel is added.  
<br> 
## 機能一覧_Functions
### インポート_Import  
  スタートアップファイルに保存されているワークスペースをインポートします。  
  Make Activeにチェックを入れると、現在のワークスペースがインポートしたワークスペースに切り替わります。  
  元に戻す(Ctrl+z)不可の操作です。  
<br>
  Import the Workspace from startup.blend.
  When Make Active is checked, current Workspace wil be switched to the imported one.  
  This operation can't undo(Ctrl+z).  
<br>
### 削除_Delete Other Workspaces  
  現在開いているワークスペース以外のワークスペースを全て削除します。  
  元に戻す(Ctrl+z)不可の操作です。  
<br>
  Delete all Workspaces except for the current active one.  
  This operation can't undo(Ctrl+z).  
<br>
## 公式の機能_Blender Functions
  本アドオンの機能はすべて公式の機能で代替できます。  
  Blenderには以下のような機能があります。  
  Blender has tha same function as this Add-on.  
### 常にスタートアップ設定のワークスペースで.blendファイルを開く  
  編集 > プリファレンス... > セーブ＆ロード > Blendファイル > UIをロード  
<br>
  Always open .blend with Startup-setting Workspaces.  
  Edit > Preference... > Sace & Load > Blend Files > Load UI  
<br>
### スタートアップ設定のWorkspaceで.blendファイルを開く  
  ファイル > 開く... > オプション（歯車マーク） > UIをロード  
<br>
  Open a .blend with Startup-setting Workspaces.  
  File > Open... > Option Load UI  
<br>
### ワークスペースを追加する  
  ワークスペースを追加（+） > 全般 > ワークスペース名  
<br>
  Add Workspace  
  Add Workspace > Genaral > Workspace name  
<br>
### ワークスペースを削除する  
  ワークスペース名を右クリック > 削除  
<br>
  Delete Workspace  
  Right Click on Workspace name > Delete  
<br>
