import asyncio

class Converter:

    @staticmethod
    async def webm2mp4(input_path, output_path):
        conversion = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-y",                      # Overwrite automaticamente il file di output se già esiste
            "-i", input_path,         # File di input (formato .webm)
            #"-vf", "scale='min(1280,iw)':'min(720,ih)':force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2" #ERRORE QUI
                                        # Filtro video ffmpeg usato per mantenere l'aspect ratio originale senza deformazioni,
                                        # adattando il video a una risoluzione fissa (es. 1280x720) e garantendo compatibilità col codec:
                                        #
                                        # -vf "scale='if(gt(iw/ih,16/9),1280,-2)':'if(gt(iw/ih,16/9),-2,720)',pad=1280:720:(ow-iw)/2:(oh-ih)/2"
                                        #
                                        # Spiegazione dettagliata:
                                        # 1) scale='if(gt(iw/ih,16/9),1280,-2)':'if(gt(iw/ih,16/9),-2,720)'
                                        #    - Confronta il rapporto larghezza/altezza (iw/ih) con il rapporto 16:9 (1280/720).
                                        #    - Se il video è più largo di 16:9 (gt = greater than), scala la larghezza a 1280 px,
                                        #      mentre l'altezza viene calcolata automaticamente (-2) mantenendo le proporzioni.
                                        #    - Se il video è più alto o uguale a 16:9, scala l'altezza a 720 px,
                                        #      mentre la larghezza viene calcolata automaticamente (-2).
                                        #    - In questo modo si mantiene sempre il rapporto d'aspetto originale senza deformazioni.
                                        #
                                        # 2) pad=1280:720:(ow-iw)/2:(oh-ih)/2
                                        #    - Aggiunge padding nero per portare il video a 1280x720 pixel fissi.
                                        #    - (ow-iw)/2 e (oh-ih)/2 centreranno il video all’interno del frame con bordi neri simmetrici.
                                        #    - Questo serve per avere una risoluzione finale standard e compatibile con la maggior parte dei player e piattaforme.
                                        #
                                        # In sintesi, questo filtro scala il video mantenendo l'aspect ratio originale,
                                        # aggiunge bordi neri solo se necessario per adattarlo a 1280x720,
                                         # e produce un file video pronto per essere codificato da libx264 senza problemi.
            "-vf", "scale=iw:ih:force_original_aspect_ratio=decrease",
                   
            "-c:v", "libx264",        # Codec video: H.264 (molto compatibile, usato ovunque)
            "-preset", "fast",        # Velocità di encoding: "fast" è un buon compromesso tra qualità e tempo
            "-crf", "23",             # Constant Rate Factor: 23 = qualità medio-alta, valore standard consigliato
            "-pix_fmt", "yuv420p",    # Formato dei pixel: garantisce compatibilità con Telegram e player mobili
            "-c:a", "aac",            # Codec audio: AAC, compatibile e leggero
            "-movflags", "+faststart",output_path,  # Sposta i metadati all'inizio del file per l'avvio immediato (streaming friendly)
            # Percorso dove salvare l’output convertito (.mp4)
        #stdout = asyncio.subprocess.DEVNULL,
        #stderr = asyncio.subprocess.DEVNULL,
        )
        await conversion.communicate()   # Attende che ffmpeg finisca il lavoro
        print('file converted (hopefully)')  # Log utile per il debug
        return conversion.returncode     # hopeffully 0 se tutto è andato bene