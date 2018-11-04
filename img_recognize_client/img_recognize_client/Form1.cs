using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using AForge;
using AForge.Controls;
using AForge.Video;
using AForge.Video.DirectShow;
using Size = System.Drawing.Size;

using System.Windows.Media.Imaging;
using System.Windows;
using System.IO;

namespace img_recognize_client
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            FilterInfoCollection videoDevices;
            videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);

            VideoCaptureDevice videoSource = new VideoCaptureDevice(videoDevices[0].MonikerString);
            videoSource.DesiredFrameSize = new System.Drawing.Size(214, 281);
            videoSource.DesiredFrameRate = 1;

            videoSourcePlayer.VideoSource = videoSource;
            videoSourcePlayer.Start();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (videoSourcePlayer.IsRunning)
            {
                string path = "e:\\";
                BitmapSource bitmapSource = System.Windows.Interop.Imaging.CreateBitmapSourceFromHBitmap(
                                    videoSourcePlayer.GetCurrentVideoFrame().GetHbitmap(),
                                    IntPtr.Zero,
                                    Int32Rect.Empty,
                                    BitmapSizeOptions.FromEmptyOptions());
                PngBitmapEncoder pE = new PngBitmapEncoder();
                pE.Frames.Add(BitmapFrame.Create(bitmapSource));
                string picName = path + "paizhao" + ".jpg";
                if (File.Exists(picName))
                {
                    File.Delete(picName);
                }
                using (Stream stream = File.Create(picName))
                {
                    pE.Save(stream);
                }
            }
        }
    }
}
